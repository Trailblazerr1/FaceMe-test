from django.conf.urls import url


from .views import *

urlpatterns = [
    url(r'^profile/',home),
    url(r'^graph/', graph),
    url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month'),

    url(r'^api/timelinejson', timelinejson, name='timelinejson'),
    url(r'^timeline', timeline, name='timeline'),

    url(r'^catch', catch, name='catch'),
    url(r'^api/catchjson0', catchjson0, name='catchjson0'),
    url(r'^api/catchjson1', catchjson1, name='catchjson1'),
    url(r'^api/catchjson2', catchjson2, name='catchjson2'),
    url(r'^api/catchjson3', catchjson3, name='catchjson3'),

    url(r'^api/lovejson0', lovejson0, name='lovejson0'),
    url(r'^api/lovejson1', lovejson1, name='lovejson1'),
    url(r'^love', love, name='love'), 
    url(r'^nations',nations,name='nations'),
]