# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 08:51:48 2017

@author: wulff
"""

import praw
import datetime
from time import mktime
import logging

# This is basic logging code provided by PRAW.  I didn't really alter anything
# here, so I don't have too much to comment on
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Here's the initialization of the 'Reddit' object.  Client ID and secret
# are given by the authorization on the reddit side.  I'll link to some stuff
# on the github readme.  The user agent is a string that gives reddit basic
# information on what you're doing.


reddit = praw.Reddit(client_id='id',
                     client_secret='secret',
                     password='Your password (may be only needed if not read only)',
                     username='Your username (again may only be needed if not read only)',
                     user_agent='windows:com.example.datestamp_search:v0.0.1 (by /u/wulffguy)')

# This is just printing out whether you're in read only mode or not
print("Read Only?")
print(reddit.read_only)
print("\n")

#print(reddit.user.me())

# The way my code works is it takes a date range as a console input and prints
# out all the search results as a basically formatted HTML page
# Since I've been the only one using it thus far, it's a bit messy

# This initializes the subreddit you'd like to search through.  I haven't tried
# it, but I believe that 'all' works as a valid sub if you want to search
# through all of reddit
sub = reddit.subreddit("science")

# Here's where the Python console takes inputs for date and converts them into
# int data types
year_s = int(input("Enter year start"))
month_s = int(input("Enter Month start"))
day_s = int(input("Enter Day start"))

year_e = int(input("Enter year end"))
month_e = int(input("Enter Month end"))
day_e = int(input("Enter Day end"))

# This creates/opens a file with string formatting as follows
file_out = open("{}_{}{}{}_{}{}{}.html".format(sub, year_s, month_s, day_s, year_e, month_e, day_e),"w")

# This converts the date values to unix-accepted values
start = datetime.date(year_s,month_s,day_s)
start = int(mktime(start.timetuple()))
print(start)

end = datetime.date(year_e,month_e,day_e)
end = int(mktime(end.timetuple()))
print(end)

# Here's the search string.  I'm interested in things involving rule changes on
# subs, so I put that in here.
searchstr = "'rule' timestamp:{}..{}".format(start,end)

# This loops through search results and writes them in the open HTML file
for submission in sub.search(searchstr,syntax='cloudsearch',limit=None):
    file_out.write("<h2>{}</h2>\n".format(submission.title))
    file_out.write("<p>Author: {}</p>\n".format(submission.author))
    file_out.write("<p>Comments: {}</p>\n".format(submission.num_comments))
    file_out.write("<p>Timestamp: {}</p>\n".format(submission.created))
    file_out.write("<p>URL: <a href=\"{}\">{}</a></p>\n\n".format(submission.url,submission.url))
    
file_out.close()