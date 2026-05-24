# Car-Value-Scraper
Python script to scrape car valuations

## A little about this project

Recently I was talking to my friend Kelly about buying a used car. They know a lot about how much cars are worth. They even have an API. Kelly though, is a little stubborn and only will give car dealers API keys. Thats fine, because they also publish their car valuations on their website. No API? No Problem.

## Do you just want the data?

Below is a little bit about the script and how to use it. If you just want the data though and don't care about everything else, I am going to point you to data.json which has all the data. The data is for "good" condition. It should be generally for the NYC metro area, but I am sure wouldn't change much. It should be accurate as of late May 2026. It is sorted by automaker, then model, then year, then trim, then selling type. Have fun with the data! Please don't make any major decisions based from this data. It's just a heuristic to understand a car's rough value. 

## How did I develop it?

At first, I naively tried using the requests library as I was taught in my introductory python class. I quickly learned this wouldn't work for a multitude of reasons and I would have to be a lot sneakier. I tried using playwright, but it didn't work amazingly. Ultimately, I landed on using PyDoll which is really an amazing library! It made scraping a dream.

When I was researching scraping methods, I also learned about identifying fetch requests and trying to reverse engineer APIs. I had slight success with this, scroll to the bottom if you would like to read more!

The way Kelly organizes their car reviews is by making the URL /make/model/year. This allows us to easily land on the pages we want. Once we are on a specific year we want, there is then a table with all the different values for the different trims. That is the table that this python script scrapes. Once I identified the CSS class that the table is in, I was able to tell PyDoll to look for that table! Once finding the table, it writes the data to a Json which nests make, models, and then years, finally with the different trims.

To get a list of all the vehicles and years the script would search, I got lazy and just had Claude write me a list. It works well and just missed out on a couple vehicles. As you'll learn later, if you want there's a way to fix it.

The last model year of a car is saved without the year, which threw off my script a little but I added a handler for this so it shouldn't be a problem.

## How do you use it? 

Firstly, you need some sort of chromium browser on your machine for PyDoll. It only works on Chromium. Apparently, it will find whatever browser you already have on your computer and drive that. I have Chrome on my computer, and it ran that just fine, if you're having problems with PyDoll, maybe try downloading Chrome. 

Next, let's set up a folder for our project. Put scraper.py and vehicle._list.py in this folder. Then setup our virtual environment in this directory and install PyDoll and pandas. If you want your own data, don't download the published data from the repo. You will soon have your own data. 

```bash
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
# or: .venv\Scripts\activate # Windows
pip install pydoll-python pandas
```

Because I am terrified of getting sued, you will have to figure out who Kelly is and replace the URL in the scraper.py on line 101 with the correct base domain. 

Before talking about configurations, I want to talk a little bit about how I attempted to avoid getting blocked. Firstly, I tried to randomize as much as I could. The time between queries is random. Additionally, instead of going on until we finish, I chunk up the requests. This makes it look less sus. Additionally, for each chunk PyDoll launches a new Chrome instance which has a fresh set of cookies and cache. There are three outcomes a request can have. A success, we got the data we wanted. Invalid, we got redirected to the wrong page. Ambiguous, we didn't get what we wanted but also didn't get redirected. The ambiguous ones are the ones that will most likely signify we are blocked. Some configuration options you have: 

1. PAGE_TIMEOUT, this is how long it takes for us to sit on a page waiting for the data we want before an ambiguous failure to be triggered
2. DELAY_MIN and _MAX, this is the range of seconds in which the script will randomly pick before going on to the next link
3. CHUNK_SIZE, this is how big your chunks are
4. CHUNK_PAUSE_MIN and _MAX, this is the range of seconds in which the script will randomly pick before going on to the next chunk
5. CONSECUTIVE_FAILURE_LIMIT, this is how many ambiguous failures we will accept before the program shuts down because it thinks that we have been blocked. We don't want to make the block worse by going even after we've been blocked.

Now that we have configured our script. Let it rip! Run `python scraper.py` and sit back. I opted for a headed experience, which means PyDoll will open a new browser on your computer every chunk. Although headless is less annoying for you, it increases the likelihood of getting blocked. It took me about 10 hours to complete every car from 2000 to 2024 in the data set I have published. If you need to stop and resume, it should gracefully handle skipping over the data we already have referring to the data.json file that already exists. If you want to skip to a specific chunk, you can also run it with `python scraper.py --start-chunk {int}` for which chunk you want to skip to. Additionally, it will refer to invalid.json which are the ones that for some reason didn't work. 

You can look over them and see why exactly they are failing. Usually, they are because they skipped a model year, or something. My code isn't perfect though and definitely doesn't handle everything amazingly. If you so wish, feel free to submit a pull request if you fix a vehicle not working for whatever reason. You can then remove this vehicle from the invalid file and it will look over it again.

The results will be for the "good" condition. The location will be the general area wherever your IP traces back to, I think. This should mean that my published data will generally be the NYC metro area, but I can't tell you the exact zip code!

## Trying to figure out API

Like I mentioned above, I did some digging in the inspection tool. I was able to see the official API, but of course, no API key. I did identify one endpoint that had the API key in the request URL 

https://upa.syndication.{kelly's car evaluations}.com/usedcar/?apikey=76a9532b-fa54-4d02-8e6a-91c3fb85376c&zipcode=12345&vehicleid=412119&pricetype=retail&condition=verygood&format=json

As far as I can tell, this API key is for all requests made from all users. I tested on multiple computers from multiple places, and they all had this key. Maybe they rotate it weekly? The problem is that this call request requires a vehicle ID. This is like a proprietary SKU for the make, model, year, and trim all in one code. I couldn't figure out a way to gather them en masse. I did figure out that if you use their compare vehicles feature, if you put a vehicle in it will show the ID in the URL bar, but that isn't enough volume for what I need. If you care enough to figure out that endpoint, it would be better for precise vehicle price monitoring, allowing for changes in other things like zip code and condition. 

## Future exploration and adaptation 

I think there is plenty more potential for this project. You could modify it to save other details on the page about the vehicle, like the ratings. You could adapt it so that instead of scraping all at once, you call it like an API. I would love to explore this data some more. A general trend I noticed as the program ran is that automakers have seemed to significantly increase the amount of trims they offer.

I also have worked on and will be posting soon a browser extension that uses this data to overlay on Facebook marketplace so you can get an idea of which vehicles are fairly priced.
