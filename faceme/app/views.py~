
from django.http import JsonResponse
from django.shortcuts import render
from .fetchdata1 import fbdata,activity,topfrnd,photo
from .fetchdata2 import *
import requests
import json
from django.http import HttpResponse
from app.models import Dog
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp


def home(request):
  #  user = request.user
  #  print(user)
  #  access_token = SocialToken.objects.get(account__user=user, account__provider='facebook')
  #  print(access_token)
   # access_token = str(access_token)
    access_token = 'EAAZAtnvu9OZCUBAIVZCJ6RIZBIQAf0keGa8ihC1btpc4IU9wnSld5kJb9whIX4UDXK6kUnOMSsdo82BDZA1rfJqA5NrWOAGZCVNCDZBJJGbb0nfZAuTy8PFSilUsLuXsy2yODoin1BQUsUiA8fGlqcQcUvRWVhDHxZBMZD'

    return access_token

def graph(request):
    tok = home(request)
    luv = lovejson0(request)
    luv0 = luv[0]
    luv1 = luv[1]
    tt = []
    for i in luv1:
        tt.append(i['value'])
    ids = photo(tok,luv0)
    return render(request, 'app/abc.html', {'js0':  luv0 , 'js1':luv1 ,'tt':tt , 'ids':ids})

def play_count_by_month(request):
    tok = home(request)
    words = ["When you thought it was over with \"Heath ledger\"!! :)\n#moriarty", "*  Before you think  *\nYou see the old fellow round the corner sneaking petrified glances at you, who averted his gaze when you spotted him. Maybe he isn't after your luggage. Possibly, you remind him of son he recently lost. How would you know, you couldn't perceive how his heart raced and moisture seeped into his grieved eyes when you smiled at him.\n\nYou see the bearded man at the last seat, who refused to oblige when you politely asked him to pull off the window. He may not be arrogant. Maybe among the clutter of thoughts hovering over his mind your request didn't stand a chance. Maybe his furrowed brows are knitting plans to gather enough money to treat his kid. You should see the medical bills poking out of his lap.\n\nYou see the young lady in the front seat, whose wrinkled saree is revealing more than intended may not be a skank. Maybe she's too tired to fight with her husband and had decided to quit. The clothes are mere illusion in the world she's going to enter. How would you know, she won't show you the burn marks on her neck.\n\nYou see that young lad in the middle whose rib-tickling anecdote was followed by a burst of laughter. His life may not be mirthful at all. Maybe, this time again, he failed to get a job. You should see how every multistorey office flames a spark in his cheeky eyes. How would you know, you haven't borne the weight of his parents' expectations.\n\nDon't judge anyone, you never know the battle they are fighting, the sacrifices they made or the chunk of soul they lost in the midway. Happy stargazing.\n\nPeace...\n~Anurag", "Skill development :D", "effe 2k16!! :)", "* The other side *\nLike love, we come in different size, shapes, caste, color and ethnicity. We are the 'Smoking kills' warning on the cigarettes or the editorial column of the newspaper whom no-one pays heed to.\nWe are the 'Mandal' from 'Pitchers' whose opinion never matters. The fellow with battered teeth, the scar-smudge faced lad, the shy guy with specs or that obese one, you see, we come in varieties. We are not different, we are just not the same.\n\nNo-one writes love songs on us and nobody calls us a hero. We don't advertise our emotions. We lower the chaos around. We are the infamous wallflowers.\n Somehow, we have the inherent talent of making girls feel uneasy, that's why we are found at the farthest corner of the class. We are, perhaps, the most adjustable creature on the planet. Our heart easily syncs with smile of yours. We strive to look different from being different but, we know, that never helps.\n\nWe are the guys whose heart skips a beat when you wave us a hi!. We could pen down a thousand musings about you but couldn't message you a single one. Our backspace key knows better of us.\nWe are the labyrinth of thoughts, an alley of scented memories or the untrodden road. We are easiest to learn but hardest to master.\n\nSo, next time when you look for your knight in shining armour, do remember the ones with stained capes.\n\nPeace..\n~Anurag", "* The confession I never wrote *\n\nSometimes, I think I don't deserve you. How could a hemlock aspire for an English vodka. The poor Aladdin was never meant for princess Jasmine. But, if only my heart could understand that. The freckles on your neck, as you are engrossed in studies, makes my heart freckle from within. I couldn't help but fall for the lonely hair-lock, swinging in air, caressing your cheek. The alluring aura of yours makes my senses spin about you all day long. We are the jumbled pieces of a jig-saw puzzle, messy chords of headphone or randomized hands of a clock, meant to be together, forever.\n\nBeneath the cloak of these words stands a guy, sober, simple and crazy enough to negotiate with time to be with you. I Know I don't fit in many check-boxes of yours, but believe me human and flaw are two complimentary words. Perfection is a word conspired by universe to keep us apart.\n\nYou know, you are terribly crazy, freak, childish dipped with innocence, the perfect amalgam He could ever create. Not to forget those dark, grim shades of grey of yours are an added perk.\n\nAnd it would happen again. This time again you will fail to read between the lines. The mask of narration won't let you decipher the message that lies beneath. Once more you would ask me \"Why do you write stories?\" and as always I wouldn't be knowing how to answer you.\n\nPeace...\n                                                          ~Anurag", "Awsm work..", "Epic!!!", "Do you believe in phantoms, ghosts, spirits or shadows? No! Think again!!!\nPenning down something supernatural......\n", "Penned down something thoughtful this time..", "This winter try love in a new flavor...\nFollow the link below:\nhttps://campusdiaries.com/stories/love-now-in-a-new-flavor", "It is said that\"College is the reward for surviving high school\".\n\nSo just tried to pen down my thoughts about 'First day at college'.\nWanna have a luk :-)\nGoto :- ", "If u hav crazzzy frnds :-) u hav everything..\n\np.c.-aseem shrey", "we created history. ...\nhttp://www.jagran.com/uttar-pradesh/bahraich-11352917.html", "A reunion worth remembering @bahraich......", "Deep jalte jagmagate rahe,\r\nHum aapko aap hame\r\nyaad aate rahe, Jab tak\r\nzindagi hai, Dua hai\r\nhamari, Aap chand ki\r\ntarah jagmagate rahe.\r\n\u201cHappy Diwali\u201d", "happy raksha bandhan to all", "nice pic", "watch this moving pic"]
    return JsonResponse(words, safe=False)

#============================================================================
def timelinejson(request):
    tok = home(request)
    data = [{"label": "status updates", "value": 4}, {"label": "photo uploads", "value": 23}, {"label": "links shared", "value": 3}]
    return JsonResponse(data, safe=False)

def timeline(request):
    return render(request, 'app/timeline.html')

#=============================================================================
def catchjson0(request):
    tok = home(request) 
    print(tok)
    #global data = activity(tok)
    dataa = [[{"label": "13", "value": 102}, {"label": "14", "value": 16}, {"label": "15", "value": 1}, {"label": "16", "value": 4}, {"label": "95", "value": 1}], [{"label": "01", "value": 3}, {"label": "02", "value": 15}, {"label": "03", "value": 6}, {"label": "04", "value": 13}, {"label": "05", "value": 11}, {"label": "06", "value": 4}, {"label": "07", "value": 5}, {"label": "08", "value": 9}, {"label": "09", "value": 1}, {"label": "10", "value": 6}, {"label": "11", "value": 12}, {"label": "12", "value": 2}, {"label": "13", "value": 4}, {"label": "14", "value": 11}, {"label": "15", "value": 2}, {"label": "16", "value": 5}, {"label": "17", "value": 10}, {"label": "18", "value": 3}, {"label": "19", "value": 2}], [{"label": "02/13", "value": 19}, {"label": "02/95", "value": 1}, {"label": "03/13", "value": 3}, {"label": "04/13", "value": 13}, {"label": "04/14", "value": 10}, {"label": "05/13", "value": 30}, {"label": "05/14", "value": 6}, {"label": "05/16", "value": 1}, {"label": "06/13", "value": 18}, {"label": "06/16", "value": 1}, {"label": "07/15", "value": 1}, {"label": "08/13", "value": 9}, {"label": "09/13", "value": 1}, {"label": "09/16", "value": 2}, {"label": "10/13", "value": 6}, {"label": "12/13", "value": 3}], [{"label": "Friday", "value": 27}, {"label": "Monday", "value": 25}, {"label": "Saturday", "value": 22}, {"label": "Sunday", "value": 12}, {"label": "Thursday", "value": 4}, {"label": "Tuesday", "value": 20}, {"label": "Wednesday", "value": 14}]]
   # p1 = Dog.objects.create(name='abcd',data=dataa)
    return JsonResponse(dataa[0], safe=False)
def catchjson1(request):
    data = Dog.objects.get(name="abcd").jdata
    return JsonResponse(data[1], safe=False)    
def catchjson2(request):
    data = Dog.objects.get(name="abcd").jdata
    return JsonResponse(data[2], safe=False)
def catchjson3(request):
    data = Dog.objects.get(name="abcd").jdata
    return JsonResponse(data[3], safe=False)

def catch(request):
    return render(request, 'app/pieperfect.html')

#=============================================================================

def lovejson0(request):
    tok = home(request)
    data = [[{'name': 'Vijay Singh', 'id': '566651146851386', 'likes': 13}, {'name': 'Chris Stein', 'id': '1805025656405878', 'likes': 1}],[{'value': 124, 'label': 'total activities'}, {'value': 2, 'label': 'max likes on a post'}, {'value': 14, 'label': 'total no of likes'}]]
    return data

def lovejson1(request):
   # tok = home(request)
    data = [[{'name': 'Vijay Singh', 'id': '566651146851386', 'likes': 13}, {'name': 'Chris Stein', 'id': '1805025656405878', 'likes': 1}],[{'value': 124, 'label': 'total activities'}, {'value': 2, 'label': 'max likes on a post'}, {'value': 14, 'label': 'total no of likes'}]]
    return JsonResponse(data[1], safe=False)

def love(request):
    tok = home(request)
    return render(request, 'app/love.html')

def nations(request):
    fi = [{"name":"Angola","region":"Sub-Saharan Africa","income":[[1800,359.93],[1820,359.93],[1913,556.12],[1950,3363.02],[1951,3440.9],[1952,3520.61],[1953,3598.81],[1954,3450.82],[1955,3672.08],[1956,3549.04],[1957,3827.94],[1958,3966.42],[1959,3917.76],[1960,4006.21],[1961,4463.83],[1962,4269.28],[1963,4413.6],[1964,4826.49],[1965,5102.21],[1966,5308.14],[1967,5522.78],[1968,5346.63],[1969,5408.12],[1970,5651.88],[1971,5526.21],[1972,5473.29],[1973,5722.02],[1974,5470.21],[1975,3430.85],[1976,3050.32],[1977,3008.65],[1978,3070.82],[1979,3064.89],[1980,3074.75],[1981,2953.41],[1982,2756.95],[1983,2584.56],[1984,2527.47],[1985,2492.83],[1986,2220.61],[1987,2430.21],[1988,2728.53],[1989,2730.56],[1990,2777.42],[1991,2730.85],[1992,2627.85],[1993,1869.92],[1994,1851.45],[1995,1989.02],[1996,2157.35],[1997,2277.14],[1998,2384.48],[1999,2417.18],[2000,2446.65],[2001,2479.69],[2002,2773.29],[2003,2785.39],[2004,3007.11],[2005,3533],[2006,4069.56],[2007,4755.46],[2008,5228.74],[2009,5055.59]],"lifeExpectancy":[[1800,26.98],[1940,26.98],[1950,29.22],[1951,29.42],[1952,29.81],[1953,30.21],[1954,30.6],[1955,31],[1956,31.4],[1957,31.8],[1958,32.2],[1959,32.6],[1960,33],[1961,33.4],[1962,33.8],[1963,34.2],[1964,34.6],[1965,35],[1966,35.4],[1967,35.8],[1968,36.2],[1969,36.6],[1970,37],[1971,37.41],[1972,37.83],[1973,38.26],[1974,38.68],[1975,39.09],[1976,39.46],[1977,39.8],[1978,40.1],[1979,40.34],[1980,40.55],[1981,40.71],[1982,40.85],[1983,40.97],[1984,41.08],[1985,41.2],[1986,41.33],[1987,41.48],[1988,41.64],[1989,41.81],[1990,41.99],[1991,42.16],[1992,42.32],[1993,42.46],[1994,42.59],[1995,42.7],[1996,42.82],[1997,42.96],[1998,43.12],[1999,43.32],[2000,43.56],[2001,43.86],[2002,44.22],[2003,44.61],[2004,45.05],[2005,45.52],[2006,46.02],[2007,46.54],[2008,47.06],[2009,47.58]]}]
    return JsonResponse(fi, safe=False)
