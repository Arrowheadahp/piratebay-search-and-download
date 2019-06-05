from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser

def soupcreate(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    #print ('url page read') 
    return(BeautifulSoup(webpage,features="lxml"))


def getmagnet(url):
    torsoup=soupcreate(url)

    link=torsoup.find('div',{'class':'download'})
    magnet=link.a.get('href')

    webbrowser.open(magnet)
    
