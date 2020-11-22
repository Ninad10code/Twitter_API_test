from django.shortcuts import redirect,render
from django.http import HttpResponse,JsonResponse
import tweepy
from . import config
# Create your views here.
auth=tweepy.OAuthHandler(config.api_key,config.api_secret_key)
auth.set_access_token(config.access_token,config.token_secret)
api = tweepy.API(auth)

def indexPage(request):    
    # return HttpResponse("Hello")
    
    
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

    
def tweets_loc(request):
    """
    docstring
    """
    search_word="#Codechella"+"-filter:retweets"
    date_since="2020-11-19"
    tweets=tweepy.Cursor(api.search,q=search_word,lang="en",since=date_since).items(10)
    # tweets_collection=[tweet.text for tweet in tweets]
    # username_collection=[tweet.user.screen_name for tweet in tweets]
    # location_collection=[tweet.user.location for tweet in tweets]

    # Collect a list of tweets
    # [tweet.text for tweet in tweets]
    collection=[[tweet.text,tweet.user.screen_name,tweet.user.location] for tweet in tweets]
    # print(collection)
    mydictionary={
        # "tweets":tweets_collection,
        "tweet_data":collection,
        "range_list":3,
    }

    return render(request,'tweets_location.html',context=mydictionary)

def particular(request):
    # search_word="#Codechella"+"-filter:retweets"
    user_id="Vedant_Bahel"
    date_since="2020-11-19"
    tweets=api.user_timeline(screen_name=user_id,count=3,include_rts=False,tweet_mode='extended')
    collection=[[tweet.id,tweet.full_text,tweet.favorite_count] for tweet in tweets]
    # print(collection)
    mydictionary={
        "tweet_info":collection,
    }
    return render(request,'particular.html',context=mydictionary)
    # for info in collection[:2]:
    #     print(info.id)
    #     print(info.full_text)
    #     print('\n')

def update(request):
    
    mytweet=request.POST['tweet_input']+" #Codechella"
    api.update_status(mytweet)

    return redirect('tweets_loc')

def group(request):
    """
    docstring
    """
    return render(request,'group.html')

    
def codechella(request):
    """
    docstring
    """
    search_word="#Codechella"+"-filter:retweets"
    date_since="2020-11-22"
    tweets=tweepy.Cursor(api.search,q=search_word,lang="en",since=date_since).items(10)
    # tweets_collection=[tweet.text for tweet in tweets]
    # username_collection=[tweet.user.screen_name for tweet in tweets]
    # location_collection=[tweet.user.location for tweet in tweets]

    # Collect a list of tweets
    # [tweet.text for tweet in tweets]
    collection=[[tweet.text,tweet.user.screen_name] for tweet in tweets]
    hashtag="Codechella"
    pathurl="codechella"
    # print(collection)
    mydictionary={
        # "tweets":tweets_collection,
        "tweet_data":collection,
        "hashtag": hashtag,
        "pathurl": pathurl,
        
    }

    return render(request,'hashtag.html',context=mydictionary)

def blm(request):
    """
    docstring
    """
    search_word="#BlackLivesMatter"+"-filter:retweets"
    date_since="2020-11-22"
    tweets=tweepy.Cursor(api.search,q=search_word,lang="en",since=date_since).items(10)
    # tweets_collection=[tweet.text for tweet in tweets]
    # username_collection=[tweet.user.screen_name for tweet in tweets]
    # location_collection=[tweet.user.location for tweet in tweets]

    # Collect a list of tweets
    # [tweet.text for tweet in tweets]
    collection=[[tweet.text,tweet.user.screen_name] for tweet in tweets]
    hashtag="BlackLivesMatter"
    pathurl="BlackLivesMatter"
    # print(collection)
    mydictionary={
        # "tweets":tweets_collection,
        "tweet_data":collection,
        "hashtag": hashtag,
        "pathurl":pathurl,
        
    }

    return render(request,'hashtag.html',context=mydictionary)

def updatetweet(request):
    """
    
    """
    hashtag="#"+request.POST['hashtag_value']
    value=request.POST['hashtag_value']
    mytweet=request.POST['tweet_input']+" "+hashtag
    pathurl=request.POST['pathurl']
    # mytweet+=request.POST['hashtag']
    api.update_status(mytweet)

    return redirect(pathurl)