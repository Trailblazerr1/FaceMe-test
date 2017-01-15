import facebook
import operator
from collections import Counter
import time
import datetime
from operator import itemgetter
import requests



#activity fun ====================================================================================================
def fbdata(tok):
    graph = facebook.GraphAPI(access_token=tok, version='2.7')
    post = graph.get_connections(id='me', connection_name='posts',limit=500)
    d = post['data']
    li =[]
    for i in d:
        li.append(i['id'])
    new = []
    lin=0
    stat=0
    album=0
    for i in li:
        ty = graph.get_object(id=i, fields='type')
        new.append(ty)
        if(ty['type']=='link'):
            lin=lin+1
        if(ty['type']=='photo'):
            album=album+1
        if(ty['type']=='status'):
            stat=stat+1

    dic = [{'label':'status updates','value':stat},
            {'label':'photo uploads','value':album},
            {'label':'links shared','value':lin},
        ]

    return dic

#top frnds============================================================================================================
def topfrnd(tok):
    graph = facebook.GraphAPI(access_token=tok, version='2.7')
    post = graph.get_connections(id='me', connection_name='posts',limit=500)
    d = post['data']
    li =[]
    for i in d:
        li.append(i['id'])
    new = []
    for i in li:
        like = graph.get_connections(id=i, connection_name='likes',limit=500)
        new.append(like['data'])
    na = []
    l=len(new)
    for i in range(0,l):
        for k in new[i]:
            na.append(k['name'])
    
    c = Counter(na)
    sor = sorted(c.items(), key=operator.itemgetter(1),reverse=True)
    zz= len(sor)
    if(zz>=5):
        zz=5
    toplike = sor[0:zz]

    fr = []

    for r in range(0,zz):
        for i in range(0,l):
            for k in new[i]:
                if(k['name']==toplike[r][0] and k['id'] not in fr):
                    fr.append(k['id'])
                    break
    sol= []
    for z in range(0,zz):
        sol.append({'name':toplike[z][0],'id':fr[z], 'likes':toplike[z][1]})

    tl = len(d)

    maxx=0
    for i in range(0,l):
        if(len(new[i]) > maxx):
           maxx = len(new[i])

    su=0
    for i in range(0,l):
        su = su+len(new[i])
    print("Data fetched :P")
    di = [{'value':tl,'label':'total activities'},
        {'value':maxx,'label':'max likes on a post'},
        {'value':su,'label':'total no of likes'}
    ]
    return sol,di
#activity timeline ===================================================================================================
def activity(tok):
    graph = facebook.GraphAPI(access_token=tok, version='2.7')
    post = graph.get_connections(id='me', connection_name='posts',limit=500)
    d = post['data']
    li =[]
    for i in d:
        li.append(i['id'])
    new = []
    tym = []
    for i in li:
        t = graph.get_connections(id=i, connection_name='', date_format='U' , limit=500)
        tym.append(t['created_time'])
    mon = []
    yr = []
    ti =[]
    dti = []
    
    for i in tym:
        t=time.strftime("%D %H:%M", time.localtime(int(i)))
        mon.append(t[0:2]+ t[5:8])
        yr.append(t[6:8])
        ti.append(t[9:11])
        dti.append(t[0:8])
    dayy = []
    
    for dt in dti:
        month, day, year = (int(x) for x in dt.split('/'))    
        ans = datetime.date(year, month, day)
        dayy.append(ans.strftime("%A"))
    print("Data fetched :P")
    yy = Counter(yr)
    tt = Counter(ti)
    mm = Counter(mon)
    dd = Counter(dayy)
    yyy=[]
    ttt=[]
    mmm=[]
    ddd=[]
    for i in yy.items():
        yyy.append({'label': i[0], 'value': i[1]})
    yyy= sorted(yyy, key=itemgetter('label'), reverse=False)

    for i in tt.items():
        ttt.append({'label': i[0], 'value': i[1]})
    ttt= sorted(ttt, key=itemgetter('label'), reverse=False)

    for i in mm.items():
        mmm.append({'label': i[0], 'value': i[1]})
    mmm= sorted(mmm, key=itemgetter('label'), reverse=False)

    for i in dd.items():
        ddd.append({'label': i[0], 'value': i[1]})
    ddd= sorted(ddd, key=itemgetter('label'), reverse=False)

    return (yyy, ttt ,mmm,ddd)

def photo(tok,luv):
    ur = []
    idd = []
    for i in luv:
        idd.append(i['id'])
    for link in idd:
        url= 'https://graph.facebook.com/'+link+'?fields=picture&access_token=' + tok
        r= requests.get(url)
        re = r.json()
        ll = re['picture']['data']['url']
        ur.append(ll)
    return ur