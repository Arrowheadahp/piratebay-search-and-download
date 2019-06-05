from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser

from getmagnet import getmagnet, soupcreate
from pbay_url import geturl

'''
https://proxtpb.art
https://proxtpb.art/s/?q=GOT&page=0&orderby=99
'''

def psearch(url,query):
    
    q=''
    for c in query:
        if c==' ':
            c='+'
        q=q+c
        
    searchurl=url+'/s/?q='+q
    return (searchurl)
    
def crawlresult(searchurl):
    pbaysoup=soupcreate(searchurl)
    
    rlist=pbaysoup.find_all('div',{'class':'detName'})
    detlist=pbaysoup.find_all('font',{'class':'detDesc'})
    torlist=[[rlist[i],detlist[i]] for i in range(len(rlist))]
    
    return (torlist)


def get_input(torlist,curl=geturl()):
    i=0
    for torname,tordet in torlist:
        print (str(i)+'\t'+torname.text+'\t'+tordet.text.replace('&nbsp;',' ')+'\n')
        i+=1
    
    i=True
    while True:
        i=input('Enter Number: ')
        if i=='':
            break
        
        torurl=curl+torlist[int(i)][0].a.get('href')
        #print (torurl)
        getmagnet(torurl)
    

if __name__=='__main__':
    curl=geturl()
    query=input('Enter Query: ')
    torlist=crawlresult(psearch(curl,query))
    get_input(torlist,curl)
    
    
    




