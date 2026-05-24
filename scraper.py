import argparse
import asyncio
import json
import random
from pathlib import Path

from pydoll.browser.chromium import Chrome

from vehicle_list import expand

OUTPUT_FILE = Path("data.json")
INVALID_FILE = Path("invalid.json")

PAGE_TIMEOUT = 15
DELAY_MIN = 2.0
DELAY_MAX = 3.0

CHUNK_SIZE = 200
CHUNK_PAUSE_MIN = 60
CHUNK_PAUSE_MAX = 180

CONSECUTIVE_FAILURE_LIMIT = 8   # only counts ambiguous failures, not redirects

ERROR_URL_MARKERS = ("error404", "/404", "page-not-found", "error.html")

def price_to_int(s: str) -> int | None:
    if not s:
        return None
    cleaned = s.replace("$", "").replace(",", "").strip()
    try:
        return int(cleaned)
    except ValueError:
        return None


def load_json(path: Path, default):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path: Path, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def already_have(data: dict, make: str, model: str, year: int) -> bool:
    return bool(data.get(make, {}).get(model, {}).get(str(year)))


def is_invalid(invalid: dict, make: str, model: str, year: int) -> bool:
    return str(year) in invalid.get(make, {}).get(model, [])


def store_data(data: dict, make: str, model: str, year: int, trims: list[dict]) -> None:
    data.setdefault(make, {}).setdefault(model, {})[str(year)] = trims


def store_invalid(invalid: dict, make: str, model: str, year: int) -> None:
    """Record a confirmed-invalid combo so we skip it on future runs."""
    years = invalid.setdefault(make, {}).setdefault(model, [])
    if str(year) not in years:
        years.append(str(year))
        years.sort()


def chunked(lst: list, size: int):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


class ScrapeOutcome:
    SUCCESS = "success"      # got trims
    INVALID = "invalid"      # confirmed bad combo (redirected to error page)
    AMBIGUOUS = "ambiguous"  # no table, no clear redirect — could be block


# ---------- Scraping ----------

class BlockedException(Exception):
    pass


def url_matches_request(current_url: str, make: str, model: str, year: int) -> bool:
    lowered = current_url.lower()
    if f"/{make.lower()}/" not in lowered or f"/{model.lower()}/" not in lowered:
        return False

    # If any 4-digit year appears in the path, it must be the one we asked for.
    # This prevents accepting redirects like /honda/fit/2019/ when we asked for 2010.
    import re
    years_in_path = re.findall(r"/(\d{4})(?:/|$)", lowered)
    if years_in_path:
        return str(year) in years_in_path

    return True


async def scrape_vehicle(tab, make: str, model: str, year: int):
    url = f"https://www.{kelly car evaluations}.com/{make}/{model}/{year}/"
    await tab.go_to(url)

    current_url = await tab.current_url

    if any(marker in current_url.lower() for marker in ERROR_URL_MARKERS):
        return ScrapeOutcome.INVALID, None, current_url

    if not url_matches_request(current_url, make, model, year):
        return ScrapeOutcome.INVALID, None, current_url

    import re
    landed_has_year = bool(re.search(r"/\d{4}(?:/|$)", current_url.lower()))
    we_were_redirected = not landed_has_year  # we requested a year, landed without one


    try:
        candidates = await tab.query(".css-1su1lr9.ee33uo30", find_all=True, timeout=PAGE_TIMEOUT)
    except Exception:

        if we_were_redirected:
            return ScrapeOutcome.INVALID, None, current_url
        return ScrapeOutcome.AMBIGUOUS, None, current_url

    if not candidates:
        if we_were_redirected:
            return ScrapeOutcome.INVALID, None, current_url
        return ScrapeOutcome.AMBIGUOUS, None, current_url


    if not isinstance(candidates, list):
        candidates = [candidates]

    table = None
    for c in candidates:
        try:
            text = (await c.text)[:300].lower()
        except Exception:
            continue
        if "trade-in" in text and "style" in text:
            table = c
            break

    if table is None:
        if we_were_redirected:
            return ScrapeOutcome.INVALID, None, current_url
        return ScrapeOutcome.AMBIGUOUS, None, current_url

    rows = await table.find(tag_name="tr", find_all=True)
    trims = []
    for row in rows:
        cells = await row.query("th, td", find_all=True)
        row_data = [(await cell.text).strip() for cell in cells]
        row_data = [c for c in row_data if c]

        if len(row_data) != 4:
            continue
        if row_data[0].lower() == "style":
            continue

        trim, trade_in, private_party, fair_purchase = row_data
        trims.append({
            "trim": trim,
            "trade_in": price_to_int(trade_in),
            "private_party": price_to_int(private_party),
            "fair_purchase_price": price_to_int(fair_purchase),
        })

    if not trims:
        return ScrapeOutcome.AMBIGUOUS, None, current_url

    return ScrapeOutcome.SUCCESS, trims, current_url


async def scrape_chunk(chunk, data, invalid, chunk_idx, total_chunks):
    consecutive_ambiguous = 0
    did_work = False

    async with Chrome() as browser:
        tab = await browser.start()

        for i, (make, model, year) in enumerate(chunk):
            label = f"[chunk {chunk_idx}/{total_chunks}, {i+1}/{len(chunk)}] " \
                    f"{make}/{model}/{year}"

            if already_have(data, make, model, year):
                print(f"{label}  SKIP (already have)")
                continue
            if is_invalid(invalid, make, model, year):
                print(f"{label}  SKIP (known invalid)")
                continue

            did_work = True
            print(f"{label}  scraping...", end=" ", flush=True)

            try:
                outcome, trims, landed_url = await scrape_vehicle(tab, make, model, year)
            except Exception as e:
                print(f"ERROR: {type(e).__name__}: {e}")
                outcome, trims = ScrapeOutcome.AMBIGUOUS, None

            if outcome == ScrapeOutcome.SUCCESS:
                consecutive_ambiguous = 0
                store_data(data, make, model, year, trims)
                save_json(OUTPUT_FILE, data)
                print(f"got {len(trims)} trims")

            elif outcome == ScrapeOutcome.INVALID:
                # Doesn't count toward block detection — this is a real "doesn't exist"
                consecutive_ambiguous = 0
                store_invalid(invalid, make, model, year)
                save_json(INVALID_FILE, invalid)
                print(f"INVALID (redirected to {landed_url[:60]}...)")

            else:  # AMBIGUOUS
                consecutive_ambiguous += 1
                print(f"no table  (ambiguous streak: {consecutive_ambiguous})")

                if consecutive_ambiguous >= CONSECUTIVE_FAILURE_LIMIT:
                    raise BlockedException(
                        f"{consecutive_ambiguous} ambiguous failures in a row — "
                        f"likely soft-blocked or IP flagged"
                    )

            if i < len(chunk) - 1:
                await asyncio.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

    return did_work


async def main(start_chunk: int = 1):
    vehicles = expand()
    print(f"Total vehicle-years in list: {len(vehicles)}")

    data = load_json(OUTPUT_FILE, {})
    invalid = load_json(INVALID_FILE, {})

    have = sum(len(yrs) for mfrs in data.values() for yrs in mfrs.values())
    bad = sum(len(yrs) for mfrs in invalid.values() for yrs in mfrs.values())
    print(f"Already have data for: {have} vehicle-years")
    print(f"Already marked invalid: {bad} vehicle-years")
    print(f"Output file:  {OUTPUT_FILE.resolve()}")
    print(f"Invalid file: {INVALID_FILE.resolve()}\n")

    chunks = list(chunked(vehicles, CHUNK_SIZE))
    total_chunks = len(chunks)

    if start_chunk < 1 or start_chunk > total_chunks:
        print(f"ERROR: start_chunk={start_chunk} is out of range (1..{total_chunks})")
        return

    if start_chunk > 1:
        print(f"Starting at chunk {start_chunk}/{total_chunks} "
              f"(skipping chunks 1..{start_chunk - 1})\n")

    for chunk_idx, chunk in enumerate(chunks, start=1):
        if chunk_idx < start_chunk:
            continue
        try:
            did_work = await scrape_chunk(chunk, data, invalid, chunk_idx, total_chunks)
        except BlockedException as e:
            print(f"\n!!! BLOCK DETECTED: {e}")
            print("Stopping. Wait at least 30 minutes (ideally a few hours) "
                  "before resuming. Consider switching networks or adding a "
                  "proxy if this keeps happening.\n")
            return

        if chunk_idx < total_chunks and did_work:
            pause = random.uniform(CHUNK_PAUSE_MIN, CHUNK_PAUSE_MAX)
            print(f"\n--- Chunk {chunk_idx}/{total_chunks} done. "
                  f"Pausing {pause:.0f}s before next session ---\n")
            await asyncio.sleep(pause)
        elif chunk_idx < total_chunks:
            print(f"--- Chunk {chunk_idx}/{total_chunks} all skipped, no pause ---")

    print("\nAll chunks complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scraper")
    parser.add_argument(
        "--start-chunk",
        type=int,
        default=1,
        help="Chunk number to start from (1-indexed). Useful for resuming "
             "past chunks you don't want to re-walk. Default: 1.",
    )
    args = parser.parse_args()

    try:
        asyncio.run(main(start_chunk=args.start_chunk))
    except KeyboardInterrupt:
        print("\nInterrupted. Progress saved — rerun to resume.")