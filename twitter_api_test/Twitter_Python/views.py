from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import tweepy
from . import config
# Create your views here.

def indexPage(request):    
    # return HttpResponse("Hello")
    auth=tweepy.OAuthHandler(config.api_key,config.api_secret_key)
    auth.set_access_token(config.token)
    api = tweepy.API(auth)
    
    return render(request,'index.html')

    