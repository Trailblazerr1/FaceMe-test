import facebook


def getwords(tok):
    graph = facebook.GraphAPI(access_token=tok, version='2.7')
    post = graph.get_connections(id='me', connection_name='posts',limit=500)
    d = post['data']
    f = open('bacon.txt', 'w')
    ww = []
    for msg in d:
        if 'message' in msg:
            f=open('bacon.txt', 'a')
            ww.append(msg['message'])
            f.write(msg['message'])
            f.write(" ")
    f.close()
    f=open('bacon.txt', 'r')
    da = f.read().replace('\n', '')
    return ww

