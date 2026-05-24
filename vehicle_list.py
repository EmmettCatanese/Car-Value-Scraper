from typing import Optional

# (start_year, end_year_inclusive_or_None_for_ongoing)
YearRange = tuple[int, Optional[int]]

CUTOFF_YEAR = 2024 

VEHICLES_BY_MAKE: dict[str, dict[str, YearRange]] = {

    # ---------------- Japanese ----------------

    "toyota": {
        "camry": (2000, None),
        "corolla": (2000, None),
        "avalon": (2000, 2022),
        "prius": (2001, None),
        "prius-c": (2012, 2019),
        "prius-v": (2012, 2017),
        "rav4": (2000, None),
        "highlander": (2001, None),
        "4runner": (2000, None),
        "sequoia": (2001, None),
        "land-cruiser": (2000, 2021),
        "tacoma": (2000, None),
        "tundra": (2000, None),
        "sienna": (2000, None),
        "yaris": (2007, 2020),
        "echo": (2000, 2005),
        "matrix": (2003, 2013),
        "venza": (2009, 2015),
        "c-hr": (2018, 2022),
        "mirai": (2016, None),
        "86": (2017, 2020),
        "gr86": (2022, None),
        "gr-supra": (2020, None),
        "crown": (2023, None),
        "grand-highlander": (2024, None),
        "bz4x": (2023, None),
    },

    "honda": {
        "civic": (2000, None),
        "accord": (2000, None),
        "fit": (2007, 2020),
        "insight": (2000, 2022),  # gaps in production
        "cr-v": (2000, None),
        "hr-v": (2016, None),
        "pilot": (2003, None),
        "passport": (2000, 2002),  # original; reintroduced 2019
        "odyssey": (2000, None),
        "ridgeline": (2006, 2014),  # reintroduced 2017
        "element": (2003, 2011),
        "s2000": (2000, 2009),
        "crosstour": (2010, 2015),
        "clarity": (2017, 2021),
        "prologue": (2024, None),
    },

    "acura": {
        "tl": (2000, 2014),
        "tsx": (2004, 2014),
        "tlx": (2015, None),
        "rl": (2000, 2012),
        "rlx": (2014, 2020),
        "ilx": (2013, 2022),
        "integra": (2023, None),  # also 2000-2001 as last gen
        "mdx": (2001, None),
        "rdx": (2007, None),
        "zdx": (2010, 2013),  # reintroduced as EV 2024
        "nsx": (2017, 2022),  # also 2000-2005
    },

    "nissan": {
        "altima": (2000, None),
        "maxima": (2000, 2023),
        "sentra": (2000, None),
        "versa": (2007, None),
        "leaf": (2011, None),
        "rogue": (2008, None),
        "rogue-sport": (2017, 2022),
        "murano": (2003, None),
        "pathfinder": (2000, None),
        "armada": (2004, None),
        "frontier": (2000, None),
        "titan": (2004, 2024),
        "xterra": (2000, 2015),
        "quest": (2000, 2017),
        "cube": (2009, 2014),
        "juke": (2011, 2017),
        "kicks": (2018, None),
        "370z": (2009, 2020),
        "350z": (2003, 2009),
        "z": (2023, None),
        "gt-r": (2009, None),
        "ariya": (2023, None),
    },

    "infiniti": {
        "g35": (2003, 2007),
        "g37": (2008, 2013),
        "q50": (2014, None),
        "q60": (2014, 2022),
        "q70": (2014, 2019),
        "m35": (2006, 2010),
        "m37": (2011, 2013),
        "ex35": (2008, 2012),
        "qx50": (2014, None),
        "qx55": (2022, None),
        "qx60": (2014, None),
        "qx70": (2014, 2017),
        "qx80": (2014, None),
        "qx30": (2017, 2019),
    },

    "mazda": {
        "mazda3": (2004, None),
        "mazda6": (2003, 2021),
        "miata": (2000, 2005),
        "mx-5-miata": (2006, None),
        "cx-3": (2016, 2021),
        "cx-30": (2020, None),
        "cx-5": (2013, None),
        "cx-50": (2023, None),
        "cx-7": (2007, 2012),
        "cx-9": (2007, 2023),
        "cx-90": (2024, None),
        "tribute": (2001, 2011),
        "rx-8": (2004, 2011),
        "mazda2": (2011, 2014),
        "mazda5": (2006, 2015),
    },

    "subaru": {
        "impreza": (2000, None),
        "wrx": (2002, None),
        "legacy": (2000, None),
        "outback": (2000, None),
        "forester": (2000, None),
        "crosstrek": (2013, None),
        "ascent": (2019, None),
        "tribeca": (2006, 2014),
        "brz": (2013, None),
        "baja": (2003, 2006),
        "solterra": (2023, None),
    },

    "mitsubishi": {
        "lancer": (2002, 2017),
        "lancer-evolution": (2003, 2015),
        "galant": (2000, 2012),
        "eclipse": (2000, 2012),
        "eclipse-cross": (2018, None),
        "outlander": (2003, None),
        "outlander-sport": (2011, None),
        "endeavor": (2004, 2011),
        "mirage": (2014, None),
        "i-miev": (2012, 2017),
    },

    # ---------------- American ----------------

    "ford": {
        "fiesta": (2011, 2019),
        "focus": (2000, 2018),
        "fusion": (2006, 2020),
        "taurus": (2000, 2019),
        "mustang": (2000, None),
        "mustang-mach-e": (2021, None),
        "escape": (2001, None),
        "edge": (2007, 2024),
        "explorer": (2000, None),
        "expedition": (2000, None),
        "bronco": (2021, None),
        "bronco-sport": (2021, None),
        "ecosport": (2018, 2022),
        "f150": (2000, None),
        "f250": (2000, None),
        "f350": (2000, None),
        "ranger": (2000, 2011),  # reintroduced 2019
        "maverick": (2022, None),
        "transit-connect": (2010, 2023),
        "flex": (2009, 2019),
        "freestyle": (2005, 2007),
        "five-hundred": (2005, 2007),
        "crown-victoria": (2000, 2011),
        "thunderbird": (2002, 2005),
        "gt": (2005, 2006),
        "windstar": (2000, 2003),
        "freestar": (2004, 2007),
        "excursion": (2000, 2005),
        "c-max": (2013, 2017),
    },

    "lincoln": {
        "ls": (2000, 2006),
        "town-car": (2000, 2011),
        "mks": (2009, 2016),
        "mkz": (2007, 2020),
        "continental": (2017, 2020),
        "zephyr": (2006, 2006),
        "navigator": (2000, None),
        "aviator": (2003, 2005),  # reintroduced 2020
        "mkt": (2010, 2019),
        "mkx": (2007, 2018),
        "mkc": (2015, 2019),
        "nautilus": (2019, None),
        "corsair": (2020, None),
    },

    "chevrolet": {
        "spark": (2013, 2022),
        "sonic": (2012, 2020),
        "cruze": (2011, 2019),
        "cobalt": (2005, 2010),
        "cavalier": (2000, 2005),  # reintroduced 2025, excluded
        "malibu": (2000, None),
        "impala": (2000, 2020),
        "monte-carlo": (2000, 2007),
        "ss": (2014, 2017),
        "camaro": (2010, None),
        "corvette": (2000, None),
        "volt": (2011, 2019),
        "bolt-ev": (2017, 2023),
        "bolt-euv": (2022, 2023),
        "trax": (2015, None),
        "trailblazer": (2002, 2009),  # reintroduced 2021
        "equinox": (2005, None),
        "blazer": (2019, None),
        "traverse": (2009, None),
        "tahoe": (2000, None),
        "suburban": (2000, None),
        "colorado": (2004, 2012),  # reintroduced 2015
        "silverado-1500": (2000, None),
        "silverado-2500": (2000, None),
        "avalanche": (2002, 2013),
        "ssr": (2003, 2006),
        "hhr": (2006, 2011),
        "uplander": (2005, 2009),
        "venture": (2000, 2005),
        "astro": (2000, 2005),
        "express": (2000, None),
        "captiva-sport": (2012, 2015),
        "city-express": (2015, 2018),
    },

    "gmc": {
        "sierra-1500": (2000, None),
        "sierra-2500": (2000, None),
        "canyon": (2004, 2012),  # reintroduced 2015
        "yukon": (2000, None),
        "yukon-xl": (2000, None),
        "acadia": (2007, None),
        "terrain": (2010, None),
        "envoy": (2002, 2009),
        "jimmy": (2000, 2001),
        "safari": (2000, 2005),
        "savana": (2000, None),
        "hummer-ev": (2022, None),
    },

    "buick": {
        "lesabre": (2000, 2005),
        "park-avenue": (2000, 2005),
        "century": (2000, 2005),
        "regal": (2000, 2004),  # reintroduced 2011-2020
        "lacrosse": (2005, 2019),
        "lucerne": (2006, 2011),
        "verano": (2012, 2017),
        "cascada": (2016, 2019),
        "rendezvous": (2002, 2007),
        "rainier": (2004, 2007),
        "terraza": (2005, 2007),
        "enclave": (2008, None),
        "encore": (2013, 2022),
        "encore-gx": (2020, None),
        "envision": (2016, None),
        "envista": (2024, None),
    },

    "cadillac": {
        "cts": (2003, 2019),
        "ats": (2013, 2019),
        "ct4": (2020, None),
        "ct5": (2020, None),
        "ct6": (2016, 2020),
        "sts": (2005, 2011),
        "dts": (2006, 2011),
        "deville": (2000, 2005),
        "seville": (2000, 2004),
        "eldorado": (2000, 2002),
        "xlr": (2004, 2009),
        "srx": (2004, 2016),
        "xt4": (2019, None),
        "xt5": (2017, None),
        "xt6": (2020, None),
        "escalade": (2000, None),
        "escalade-esv": (2003, None),
        "escalade-ext": (2002, 2013),
        "lyriq": (2023, None),
    },

    "chrysler": {
        "300": (2005, 2023),
        "300m": (2000, 2004),
        "sebring": (2000, 2010),
        "200": (2011, 2017),
        "pt-cruiser": (2001, 2010),
        "town-and-country": (2000, 2016),
        "pacifica": (2017, None),
        "voyager": (2020, 2022),  # also 2000-2003
        "crossfire": (2004, 2008),
        "aspen": (2007, 2009),
        "concorde": (2000, 2004),
        "lhs": (2000, 2001),
    },

    "dodge": {
        "neon": (2000, 2005),
        "stratus": (2000, 2006),
        "caliber": (2007, 2012),
        "dart": (2013, 2016),
        "avenger": (2008, 2014),
        "charger": (2006, None),
        "challenger": (2008, None),
        "magnum": (2005, 2008),
        "intrepid": (2000, 2004),
        "viper": (2000, 2017),
        "caravan": (2000, 2007),
        "grand-caravan": (2000, 2020),
        "journey": (2009, 2020),
        "nitro": (2007, 2012),
        "durango": (2000, None),
        "dakota": (2000, 2011),
        "ram-1500": (2000, 2010),  # became Ram brand after
        "hornet": (2023, None),
    },

    "jeep": {
        "wrangler": (2000, None),
        "cherokee": (2014, 2023),
        "grand-cherokee": (2000, None),
        "grand-cherokee-l": (2021, None),
        "liberty": (2002, 2012),
        "compass": (2007, None),
        "patriot": (2007, 2017),
        "renegade": (2015, 2023),
        "gladiator": (2020, None),
        "wagoneer": (2022, None),
        "grand-wagoneer": (2022, None),
        "commander": (2006, 2010),
    },

    "ram": {
        "1500": (2011, None),
        "2500": (2011, None),
        "3500": (2011, None),
        "promaster": (2014, None),
        "promaster-city": (2015, 2022),
    },

    "tesla": {
        "model-s": (2012, None),
        "model-3": (2017, None),
        "model-x": (2016, None),
        "model-y": (2020, None),
        "roadster": (2008, 2012),
        "cybertruck": (2024, None),
    },

    # ---------------- European ----------------

    "bmw": {
        "2-series": (2014, None),
        "3-series": (2000, None),
        "4-series": (2014, None),
        "5-series": (2000, None),
        "6-series": (2004, 2019),
        "7-series": (2000, None),
        "8-series": (2019, None),
        "z3": (2000, 2002),
        "z4": (2003, None),
        "z8": (2000, 2003),
        "m2": (2016, None),
        "m3": (2001, None),
        "m4": (2015, None),
        "m5": (2000, None),
        "m6": (2006, 2019),
        "m8": (2020, None),
        "x1": (2013, None),
        "x2": (2018, None),
        "x3": (2004, None),
        "x4": (2015, None),
        "x5": (2000, None),
        "x6": (2008, None),
        "x7": (2019, None),
        "i3": (2014, 2021),
        "i4": (2022, None),
        "i7": (2023, None),
        "i8": (2014, 2020),
        "ix": (2022, None),
    },

    "mercedes-benz": {
        "c-class": (2000, None),
        "e-class": (2000, None),
        "s-class": (2000, None),
        "cla": (2014, None),
        "cls": (2006, 2023),
        "clk": (2000, 2009),
        "sl": (2000, None),
        "slc": (2017, 2020),
        "slk": (2000, 2016),
        "amg-gt": (2016, None),
        "gla": (2015, None),
        "glb": (2020, None),
        "glc": (2016, None),
        "gle": (2016, None),  # was M-Class before
        "m-class": (2000, 2015),
        "gls": (2017, None),  # was GL-Class
        "gl-class": (2007, 2016),
        "g-class": (2002, None),
        "glk": (2010, 2015),
        "metris": (2016, 2023),
        "sprinter": (2003, None),
        "eqs": (2022, None),
        "eqe": (2023, None),
        "eqb": (2022, None),
        "eqs-suv": (2023, None),
    },

    "audi": {
        "a3": (2006, None),
        "a4": (2000, None),
        "a5": (2008, None),
        "a6": (2000, None),
        "a7": (2012, None),
        "a8": (2000, None),
        "s3": (2015, None),
        "s4": (2000, None),
        "s5": (2008, None),
        "s6": (2003, None),
        "s7": (2013, None),
        "s8": (2001, None),
        "rs3": (2017, None),
        "rs5": (2013, None),
        "rs6": (2003, None),
        "rs7": (2014, None),
        "tt": (2000, 2023),
        "r8": (2008, 2023),
        "q3": (2015, None),
        "q5": (2009, None),
        "q7": (2007, None),
        "q8": (2019, None),
        "sq5": (2014, None),
        "sq7": (2017, None),
        "sq8": (2020, None),
        "e-tron": (2019, 2023),
        "q4-e-tron": (2022, None),
        "q8-e-tron": (2024, None),
        "e-tron-gt": (2022, None),
    },

    "volkswagen": {
        "jetta": (2000, None),
        "passat": (2000, 2022),
        "golf": (2000, 2021),
        "gti": (2006, None),
        "golf-r": (2012, None),
        "beetle": (2000, 2019),
        "cc": (2009, 2017),
        "eos": (2007, 2016),
        "rabbit": (2006, 2009),
        "phaeton": (2004, 2006),
        "tiguan": (2009, None),
        "atlas": (2018, None),
        "atlas-cross-sport": (2020, None),
        "touareg": (2004, 2017),
        "id4": (2021, None),
        "arteon": (2019, 2023),
        "routan": (2009, 2014),
    },

    "porsche": {
        "911": (2000, None),
        "boxster": (2000, 2016),  # reborn as 718
        "cayman": (2006, 2016),   # reborn as 718
        "718-boxster": (2017, None),
        "718-cayman": (2017, None),
        "panamera": (2010, None),
        "cayenne": (2003, None),
        "macan": (2015, None),
        "taycan": (2020, None),
        "carrera-gt": (2004, 2006),
    },

    "volvo": {
        "s40": (2000, 2011),
        "s60": (2001, None),
        "s70": (2000, 2000),
        "s80": (2000, 2016),
        "s90": (2017, None),
        "v40": (2000, 2004),
        "v50": (2005, 2011),
        "v60": (2015, None),
        "v70": (2000, 2010),
        "v90": (2018, None),
        "c30": (2008, 2013),
        "c70": (2000, 2013),
        "xc40": (2019, None),
        "xc60": (2010, None),
        "xc70": (2003, 2016),
        "xc90": (2003, None),
    },

    "jaguar": {
        "x-type": (2002, 2008),
        "s-type": (2000, 2008),
        "xj": (2000, 2019),
        "xf": (2009, 2024),
        "xe": (2017, 2020),
        "xk": (2000, 2015),
        "f-type": (2014, 2024),
        "f-pace": (2017, None),
        "e-pace": (2018, None),
        "i-pace": (2019, None),
    },

    "land-rover": {
        "discovery": (2000, None),
        "discovery-sport": (2015, None),
        "lr2": (2008, 2015),
        "lr3": (2005, 2009),
        "lr4": (2010, 2016),
        "freelander": (2002, 2005),
        "defender": (2020, None),
        "range-rover": (2000, None),
        "range-rover-sport": (2006, None),
        "range-rover-evoque": (2012, None),
        "range-rover-velar": (2018, None),
    },

    "mini": {
        "cooper": (2002, None),               # Hardtop 2 Door
        "hardtop-4-door": (2015, None),       # 4-door variant, separate URL on KBB
        "convertible": (2005, None),
        "clubman": (2008, 2024),
        "countryman": (2011, None),
    },

    "fiat": {
        "500": (2012, 2019),
        "500l": (2014, 2020),
        "500x": (2016, 2023),
        "500e": (2013, None),
        "124-spider": (2017, 2020),
    },

    "alfa-romeo": {
        "4c": (2015, 2020),
        "giulia": (2017, None),
        "stelvio": (2018, None),
        "tonale": (2024, None),
    },

    # ---------------- Korean ----------------

    "hyundai": {
        "accent": (2000, 2022),
        "elantra": (2000, None),
        "sonata": (2000, None),
        "azera": (2006, 2017),
        "veloster": (2012, 2022),
        "ioniq": (2017, 2022),
        "ioniq-5": (2022, None),
        "ioniq-6": (2023, None),
        "tucson": (2005, None),
        "santa-fe": (2001, None),
        "santa-cruz": (2022, None),
        "palisade": (2020, None),
        "venue": (2020, None),
        "kona": (2018, None),
        "nexo": (2019, None),
        "entourage": (2007, 2009),
        "veracruz": (2007, 2012),
        "genesis": (2009, 2016),  # later became Genesis brand
        "genesis-coupe": (2010, 2016),
        "equus": (2011, 2016),
        "tiburon": (2000, 2008),
        "xg300": (2001, 2001),
        "xg350": (2002, 2005),
    },

    "kia": {
        "rio": (2001, 2023),
        "forte": (2010, None),
        "optima": (2001, 2020),
        "k5": (2021, None),
        "cadenza": (2014, 2020),
        "k900": (2015, 2020),
        "stinger": (2018, 2023),
        "soul": (2010, None),
        "ev6": (2022, None),
        "ev9": (2024, None),
        "niro": (2017, None),
        "sportage": (2000, None),
        "sorento": (2003, None),
        "telluride": (2020, None),
        "seltos": (2021, None),
        "carnival": (2022, None),
        "sedona": (2002, 2021),
        "rondo": (2007, 2010),
        "amanti": (2004, 2009),
        "borrego": (2009, 2009),
        "spectra": (2000, 2009),
        "sephia": (2000, 2001),
        "magentis": (2001, 2001),
    },

    "genesis": {
        "g70": (2019, None),
        "g80": (2017, None),
        "g90": (2017, None),
        "gv60": (2023, None),
        "gv70": (2022, None),
        "gv80": (2021, None),
    },
}


def expand(cutoff_year: int = CUTOFF_YEAR, start_year: int = 2000) -> list[tuple[str, str, int]]:
    """
    Expand the nested year-range structure into a flat list of
    (manufacturer, model, year) tuples ready to feed to the scraper.
    """
    out: list[tuple[str, str, int]] = []
    for make, models in VEHICLES_BY_MAKE.items():
        for model, (yr_start, yr_end) in models.items():
            yr_end_effective = yr_end if yr_end is not None else cutoff_year
            yr_end_effective = min(yr_end_effective, cutoff_year)
            yr_start_effective = max(yr_start, start_year)
            for year in range(yr_start_effective, yr_end_effective + 1):
                out.append((make, model, year))
    return out


if __name__ == "__main__":
    vehicles = expand()
    print(f"Total vehicle-years: {len(vehicles)}")
    print(f"Total unique models: {sum(len(m) for m in VEHICLES_BY_MAKE.values())}")
    print(f"Total manufacturers: {len(VEHICLES_BY_MAKE)}")
    print("\nFirst 10:")
    for v in vehicles[:10]:
        print(f"  {v}")
    print("\nLast 10:")
    for v in vehicles[-10:]:
        print(f"  {v}")