# datestamp_search
A simple and messy datestamp search on reddit using Cloudsearch
## Resources
The two things you'll need from this are the reddit authentication and an IDE. The reddit authentication is at the link below. From this, you'll need to get the id and the secret:
<https://www.reddit.com/prefs/apps/>
If you don't have a Python IDE, there are a number that can be downloaded. The easiest one to get is the one that comes packaged with Python, called IDLE. Just head to <https://www.python.org/> and grab it from there.

### Other Resources
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
Next register on reddit using the reddit link in the Resources.  If you need more help on that, you can consult the authentation help in the Resources.  There should be places on the Python script to throw the client id and secret when starting the reddit instance.  Finally, I'd put a test subreddit where the `sub = ` declaration is and run.  The console should prompt you to put in date ranges.

Feel free to contact me if you have any questions. I'm [/u/wulffguy](https://reddit.com/u/wulffguy) on reddit and [keenan.wulff@colorado.edu](mailto:keenan.wulff@colorado.edu) by email
