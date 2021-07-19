import os, time, json
from datetime import datetime
from random import randint
from tqdm import tqdm
from facebook_scraper import *
from pandas import pandas as pd
import requests


class FriendListScraper:

    def getFriends(self,username,cookies):
        set_cookies(cookies)
        friends=get_friends(username, timeout=100)
        allFriends=[]
        while True:
            try:
                friend=next(friends)
                allFriends.append(friend)
                time.sleep(0.01)
            except exceptions.TemporarilyBanned:
                print("temporary banned")
                time.sleep(600)
            except StopIteration:
                return allFriends
                break
        return allFriends




