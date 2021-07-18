from facebook_scraper import *
import json, time, facebook_scraper

class PostScraper:

 def getPosts(self,username,scookies):
        options_dict = {"posts_per_page": 200}
        allPosts=[]
        posts=get_posts(username, pages=None, cookies=scookies, extra_info=True,youtube_dl=True, options=options_dict)
        while True:
            try:
                post= next(posts)
                allPosts.append(post)
                time.sleep(0.01)
            except exceptions.TemporarilyBanned as e:
                print("Rate limit error:")
                time.sleep(60 * 15)
                continue
            except StopIteration:
                return allPosts
                break
            else:
                continue
        return allPosts


 def getUserPosts(self,Scookies,pusername,kwargs2):
    dic=self.getPosts(pusername,Scookies)
    ans=[]
    for post in dic:
        finalPost={}
        for key, value in kwargs2.items():
            if(value==True and (key in post.keys())):
                finalPost[key]=(post[key])
        ans.append(finalPost)
    return ans

