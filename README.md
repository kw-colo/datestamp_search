# datestamp_search
Reddit has changed its search service away from Amazon's Cloudsearch. This has the consequence of not allowing frontend searches involving datestamps. It is, however, still possible to default to Cloudsearch through Reddit's API. Below is an implementation for that, using a Python-based API wrapper called PRAW.

## Terms
* PRAW - This is a wrapper for Reddit's API (Application Programming Interface) that allows us to use a Python script to interact with Reddit. If you're interested, you can do much more interesting things than a simple search with PRAW (check out the quick start PRAW documentation if you're interested)
* IDE - Integrated Development Environment. This allows an integrated way to build and run Python scripts. An IDE is not strictly needed (you can do everything you need with a command line and text editor), but it's nice to have everything in one place.

## Resources
There are only two things you'll need to be able to use this: Authentication from Reddit and an IDE.

The link below is Reddit's Applications page. To use this, you'll need to register it as an application on Reddit's end, then grab the client id, which is the alphanumeric key displayed below the title of the application, and the secret, which is displayed in the details of the the application (you should see it if you hit the edit hyperlink).
<https://www.reddit.com/prefs/apps/>

Finally, if you don't have a Python IDE, there are a number that can be downloaded. The easiest one to get is the one that comes packaged with Python, called IDLE. Just head to <https://www.python.org/> and grab it from there.

### Other Resources
None of these are necessary; they're just there if you want to learn more.

This is the PRAW quick start.  This gives a basis for opening an instance, and what's needed for a read only instance
<http://praw.readthedocs.io/en/latest/getting_started/quick_start.html>

This should tell you how to authenticate your script
<http://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth>

Here's some official reddit documentation on the API.  This gives the parameters for the user agent string
<https://github.com/reddit/reddit/wiki/API>

## Getting Started
The first thing you'll need to do is install PRAW.  Through a Python command line, type
```
$ pip install praw
```
Next go to the link in the Resources section and register an application there. Once you have the client id and secret, it should be straightforward to follow the TODOs in the python script. The console should prompt you to put in date ranges.

Feel free to contact me if you have any questions. I'm [/u/wulffguy](https://reddit.com/u/wulffguy) on reddit and [keenan.wulff@colorado.edu](mailto:keenan.wulff@colorado.edu) by email
