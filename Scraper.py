

from PostScraper import *
from ProfileScraper import *
import time


class Scraper:

    def _init_(self):
        self.postScraper=PostScraper()
        self.profileScraper=ProfileScraper()



    def getUserInfo(self,cookies,Scrape_Posts,Scrape_profile,username,kwargs11, kwargs22):
        self.postScraper=PostScraper()
        dictionary={}
        if(Scrape_profile==False):
            dictionary["AllPosts"]=self.postScraper.getUserPosts(Scookies=cookies,pusername=username,kwargs2=kwargs11)
            dictionary["Username"]=username
            return dictionary
        self.profileScraper=ProfileScraper()
        dic1=self.profileScraper.getUserProfile(Scookies=cookies,usernamep=username,kwargs1=kwargs22)
        if(Scrape_Posts==True):
            dic2=self.postScraper.getUserPosts(Scookies=cookies,pusername=username,kwargs2=kwargs11)
            dic1["AllPosts"]=(dic2)
        return dic1


    def scrapeUsers(self,Scookies,users, kwargs1, kwargs2,Scrape_Posts,Scrape_profile):
        allUsers=[]
        for user in users:
            dicUser=self.getUserInfo(Scookies,Scrape_Posts,Scrape_profile,user,kwargs1,kwargs2)
            allUsers.append(dicUser)
            time.sleep(2)
        return allUsers




