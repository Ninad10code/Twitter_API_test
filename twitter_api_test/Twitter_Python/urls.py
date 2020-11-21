from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexPage,name="indexPage"),
    path('tweets_loc',views.tweets_loc,name="tweets_loc"),
    path('particular',views.particular,name="particular"),
]