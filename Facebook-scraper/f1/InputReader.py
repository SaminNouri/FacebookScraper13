from    Scraper import *
from SaveInfo import *
import json


class InputReader:


    def readUsers(self,path,str):
        if(str==None):
            str='\n'
        text_file = open(path, "r")
        lines = text_file.read().split(str)
        return lines



    def readFeatures(self,path):
        f = open(path,'r')
        data = json.load(f)
        return data

    def readData(self,args):

        self.Scrape_Posts=True
        if(args.posts!=None):
               self.postsFeatureDictionary=self.convertListToDictionary(args.posts)
        elif(args.postPath != None):
               self.postsFeatureDictionary=self.readFeatures(args.postPath[0])
        else:
               self.postsFeatureDictionary={}
               self.Scrape_Posts=False


        self.Scrape_profile=True
        if(args.profile!=None):
               self.profFeatureDictionary=self.convertListToDictionary(args.profile)
        elif(args.profilePath != None):
               self.profFeatureDictionary=self.readFeatures(args.profilePath[0])
        else:
               self.Scrape_profile=False
               self.profFeatureDictionary={}

        if(args.Users!=None):
               self.users=self.readUsers(args.Users[0],args.Users[1])
               print(self.users)
        else:
               self.users=[]

        self.outputInfo=self.readFeatures(args.outputPath[0])

        s=Scraper()
        ans=s.scrapeUsers(Scookies=args.cookies[0],users=self.users,kwargs1=self.postsFeatureDictionary,kwargs2=self.profFeatureDictionary,Scrape_Posts=self.Scrape_Posts,Scrape_profile=self.Scrape_profile)
        i=SaveInfo()
        i.saveToDataBase(ans,self.outputInfo.get('cluster'),self.outputInfo.get('database'),self.outputInfo.get('collection'))
        print("Saved to database successfully!")



    def convertListToDictionary(listt):
        dic={}
        for i in listt:
            dic[i]=True
        return dic

