from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import tweepy
from . import config
# Create your views here.

def indexPage(request):    
    # return HttpResponse("Hello")
    auth=tweepy.OAuthHandler(config.api_key,config.api_secret_key)
    auth.set_access_token(config.access_token,config.token_secret)
    api = tweepy.API(auth)
    
    ids = api.followers_ids(screen_name='ninad_dadmal',count=30)
    myFollowers=[]
    for users in api.lookup_users(user_ids=ids):
        # print("https://twitter.com/{}".format(users.screen_name))
        myFollowers.append(users.screen_name)
    mydictonary={
        "myFollowers":myFollowers,
    }
    # print(myFollowers)
    return render(request,'index.html',context=mydictonary)

    