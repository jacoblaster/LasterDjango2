from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.conf.urls.defaults import *
import datetime


# Create your views here.
def main(request):
    return HttpResponse("Hello, Hillary and Trump, the current date and time is: ");



# returns current time in html
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def main():
    # maps url to current_datetime func
    urlpatterns = patterns('',
        (r'^time/$', current_datetime),
    )

if __name__ == '__main__':
  main()
