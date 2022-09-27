#!/usr/bin/env python3
"""
Test the Scraper class.
"""

__author__ = "Jason Beach"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import sys
from pathlib import Path

sys.path.append(Path('..').absolute().as_posix() ) 

from graphipy.graphipy import GraphiPy
from graphipy.api.reddit_api import Reddit

from dotenv import load_dotenv
load_dotenv()
 


# dotenv
reddit_api_credentials = {
    "client_id": os.getenv('CLIENT_ID'),
    "client_secret": os.getenv('CLIENT_SECRET'),
    "user_agent": os.getenv('USER_AGENT'),
    "username": os.getenv('USERNAME'),
    "password": os.getenv('PASSWORD')
}


def test_init():
    sub_reddits = ['banks']
    reddit = Reddit(reddit_api_credentials)
    graphipy = GraphiPy()   #create GraphiPy object (default to Pandas)
    subreddit_submissions = reddit.fetch_subreddit_submissions(
                                graphipy.create_graph(), 
                                subreddit_name=sub_reddits[0], 
                                limit=100)
    assert True == True