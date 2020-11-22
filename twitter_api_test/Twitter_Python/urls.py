from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexPage,name="indexPage"),
    path('tweets_loc',views.tweets_loc,name="tweets_loc"),
    path('particular',views.particular,name="particular"),
    path('update',views.update,name="update"),
    path('group',views.group,name="group"),
    path('codechella',views.codechella,name="codechella"),
    path('BlackLivesMatter',views.blm,name="BlackLivesMatter"),
    path('updatetweet',views.updatetweet,name="updatetweet"),

]