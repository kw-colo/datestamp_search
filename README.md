# datestamp_search
A simple and messy datestamp search on reddit using Cloudsearch
## Resources
<http://praw.readthedocs.io/en/latest/getting_started/quick_start.html>

This is the PRAW quick start.  This gives a basis for opening an instance, and what's needed for a read only instance

<http://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth>

This should tell you how to authenticate your script

<https://www.reddit.com/prefs/apps/>

This is the reddit-side authentication portal.  You'll need to go through registration here to get your id and secret

<https://github.com/reddit/reddit/wiki/API>

Here's some official reddit documentation on the API.  This gives the parameters for the user agent string

If you don't have a Python IDE, there are a number that can be downloaded.  I'm using Anaconda through the Spyder IDE (I'm a student who is also using python to do math stuff), but any IDE should work (I haven't experimented with many but PyCharm and the PyDev plugin for Eclipse seem to be pretty popular)
## Getting Started
The first thing you'll need to do is install PRAW.  Through a Python command line, type
```
$ pip install praw
```
Next register on reddit using the reddit link in the Resources.  If you need more help on that, you can consult the authentation help in the Resources.  There should be places on the Python script to throw the client id and secret when starting the reddit instance.  Finally, I'd put a test subreddit where the `sub = ` declaration is and run.  The console should prompt you to put in date ranges.

Feel free to contact me if you have any questions
