from django.shortcuts import render
from django.http import HttpResponse
from .models import Videos
from YoutubeApiApp import settings
from datetime import datetime, timedelta

# Google API client is required connecting to YouTube Data API v3
from googleapiclient.discovery import build
from apiclient.errors import HttpError


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


from .models import Videos
from .serializers import VideosSerializer

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def fetch_new_videos(request):
    try:


        apikeys = settings.API_KEYS                   
        current_time = datetime.now()                 
    
    # Since we need to get the posts which were posted 5 minutes from current_time
        req_time = current_time - timedelta(minutes=5)
    
    # flag variable ensures the successful fetching of the videos.
        flag=False
        for apikey in apikeys:
          try:

            # Using the documentation provided here : https://developers.google.com/youtube/v3/quickstart/python
            # Called the youtube API as follows
            youtube = build("youtube", "v3", developerKey=apikey)
           
            # The predefined query is 'cricket' here, calling an instance of the same
            req = youtube.search().list(q="cricket",part="snippet", order="date",
                                        maxResults=50, publishedAfter=(req_time.replace(microsecond=0).isoformat()+'Z') )
            response = req.execute()
          
            flag=True
            for obj in response['items']:
                title = obj['snippet']['title']
                description = obj['snippet']['description']
                publishingDateTime = obj['snippet']['publishedAt']
                thumbnailsUrls = obj['snippet']['thumbnails']['default']['url']
                channelTitle = obj['snippet']['channelTitle']

                # Saving the details in the model of the DB
                Videos.objects.create(title=title, description=description,
                        publishingDateTime=publishingDateTime, thumbnailsUrls=thumbnailsUrls,
                        channelTitle=channelTitle)

        # If the quota for an api key is not exceeded keep on using the same key
          except HttpError as er:
            err_code = er.resp.status
            if not(err_code == 400 or err_code == 403):
                break

          if flag:
             break
        
        return HttpResponse("New videos have been fetched! Refresh Localhost to view added videos")
    except:
        return HttpResponse("Some error encountered")

class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   
    # Adding the search and filter fields
    search_fields = ['title']
    filter_fields = ['channelTitle']

    # For sorting the videos' data in reverse chronological order by default
    ordering = ['-publishingDateTime']
    serializer_class = VideosSerializer
    pagination_class = PageNumberPagination
