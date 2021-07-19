from facebook_scraper import *
import json, time, facebook_scraper
from FriendList import *

class ProfileScraper:


    def getUserProfile(self,Scookies,usernamep,kwargs1):
        while True:
            try:
                dic=get_profile(usernamep, cookies=Scookies)
                break
            except exceptions.TemporarilyBanned as e:
               print("Rate limit error:")
               time.sleep(60 * 15)
               continue
            else:
               continue
        ans={}
        for key, value in kwargs1.items():
            if(key in dic.keys()==False):
                continue
            if(value==True and (key in dic.keys())):
                ans[key]=(dic[key])
            if(value==True and key=='Friends'):
                Fr= FriendListScraper()
                friends=Fr.getFriends(usernamep,Scookies)
                ans['Friends']=friends
        return ans



