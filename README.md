# YoutubeVideoFetchApi

# Created a project YoutubeApiApp and inside it an app api
## 2 function inside views.py of api app folder 
### 1 for fetching videos that were posted 5 min from current time this time can be choosen as per the requirement
#### Endpoint--> http://127.0.0.1:8000/
### 2 for fetching latest videos that were stored in the database in chronological order of there published date
#### Endpoint--> http://127.0.0.1:8000/new

# Steps for setup 
## Clone the repo
## Install all dependency as per given in requirement.txt
## Generate your youtube apikeys and replace it with apikeys in the settings.py file under YoutubeApiApp folder [Link](https://developers.google.com/youtube/v3/getting-started)
## Python manage.py runserver
## Call the server with the above given endpoints

### To make a task periodic crontab module is used [Link](https://django-cron.readthedocs.io/en/latest/introduction.html) however there are some issues for setting this in windows so after successful setting of this package we can simply take getallvideos function from api/views.py  and paste it inside a cron.py following this procedure[Link](https://django-cron.readthedocs.io/en/latest/installation.html) and make that function call periodically as per requirement
