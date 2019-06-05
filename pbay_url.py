from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser

def soupcreate(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    #print ('url page read') 
    return(BeautifulSoup(webpage,features="lxml"))


def geturl():
    proxylist=soupcreate('https://piratebay-proxylist.se/')

    #proxy=proxylist.find('tr',{'class':'odd'})

    #proxyurl=proxy.get('data-probe')

    proxy=proxylist.find('td',{'class':'url'})
    proxyurl=proxy.get('data-href')

    return (proxyurl)

    



if __name__=='__main__':
    #print (geturl())
    webbrowser.open(geturl())


