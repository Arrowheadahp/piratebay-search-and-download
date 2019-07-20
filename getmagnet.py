from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import webbrowser

def soupcreate(url):
    print ('Opening Url: '+url) 
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    print ('URL opened')
    return(BeautifulSoup(webpage,features="lxml"))
'''
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print ('URL page read')
    return(BeautifulSoup(html,features="lxml"))'''


def getmagnet(url):
    torsoup=soupcreate(url)

    link=torsoup.find('div',{'class':'download'})
    magnet=link.a.get('href')

    webbrowser.open(magnet)
    
