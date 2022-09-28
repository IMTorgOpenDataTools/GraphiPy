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


def test_fetch_subreddit_submissions():
    sub_reddits = ['banks']
    reddit = Reddit(reddit_api_credentials)
    graphipy = GraphiPy()   #create GraphiPy object (default to Pandas)
    subreddit_submissions = reddit.fetch_subreddit_submissions(
                                graphipy.create_graph(), 
                                subreddit_name=sub_reddits[0], 
                                limit=10)
    keys = list(subreddit_submissions.get_nodes().keys())
    assert keys == ['subreddit', 'redditor', 'submission']


def test_fetch_submission_comments():
    ids = ['l6z41y', 'q1ni44', 'duvawt', 'dqmui2', 'docpl1', 'dny2p4', 'dm92r4', 'db758h', 'czscsj', 'cybdf2', 'ctt4ec', 'csw4dd', 'csui1s', 'cht6zv',
        'cht6zv', 'cfdsds', 'c7g63t', 'c7ezh7', 'c2xf2t', 'busdci', 'bn6rcp' 'bl80jx', 'bi03ef', 'b9ajn5', 'b2reib', 'b02h8k', 'ar064o', 'aqov78', 'aop98p', 
        'aocuw3', 'akf7v4', 'ak9yif', 'aggp1r', 'ae71z5', 'ada6cv', 'aa96g0', 'a52zm2'
        ]
    reddit = Reddit(reddit_api_credentials)
    graphipy = GraphiPy()   #create GraphiPy object (default to Pandas)
    results = []
    expected_key_list = ['submission', 'subreddit', 'redditor']
    for id in ids:
        print(id)
        subreddit_comments = reddit.fetch_submission_comments(
                                    graphipy.create_graph(), 
                                    submission_id=id, 
                                    limit=10)
        if subreddit_comments == None:
            results.append( True )
        else:
            keys = list(subreddit_comments.get_nodes().keys())
            result = [item in keys for item in expected_key_list]
            results.append( all(result)==True )
    assert all(results) == True