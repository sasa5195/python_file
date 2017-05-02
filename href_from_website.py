##import httplib2
##from BeautifulSoup import BeautifulSoup, SoupStrainer
##
##http = httplib2.Http()
##status, response = http.request('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html')
##
##for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
##    if link.has_attr('href'):
##        print link['href']
##from BeautifulSoup import BeautifulSoup
##import urllib2
##import re
##
##html_page = urllib2.urlopen("https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html")
##soup = BeautifulSoup(html_page)
##for link in soup.findAll('a'):
##    print link.get('href')
#!/usr/bin/env python
 
# get_links.py
 
##import re
##import sys
##import urllib
##import urlparse
##from BeautifulSoup import BeautifulSoup
## 
##class MyOpener(urllib.FancyURLopener):
##    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
## 
##def process(url):
##    myopener = MyOpener()
##    #page = urllib.urlopen(url)
##    page = myopener.open(url)
## 
##    text = page.read()
##    page.close()
## 
##    soup = BeautifulSoup(text)
## 
##    for tag in soup.findAll('a', href=True):
##        tag['href'] = urlparse.urljoin(url, tag['href'])
##        print tag['href']
### process(url)
## 
##def main():
##    if len(sys.argv) == 1:
##        print "Jabba's Link Extractor v0.1"
##        print "Usage: %s URL [URL]..." % sys.argv[0]
##        sys.exit(-1)
##    # else, if at least one parameter was passed
##    for url in sys.argv[1:]:
##        process(url)
### main()
## 
##if __name__ == "__main__":
##    main()


##import requests
##from BeautifulSoup import BeautifulSoup
##
##def getURL(page):
##    start_link = page.find("a href")
##    if start_link == -1:
##        return None, 0
##    start_quote = page.find('"', start_link)
##    end_quote = page.find('"', start_quote + 1)
##    url = page[start_quote + 1: end_quote]
##    return url
##url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/"
##pth="flhxd.html"
##while True:
##    response = requests.get(url+pth)
##    # parse html
##    page = str(BeautifulSoup(response.content))
##    pth = getURL(page)
##    if url+pth:
##        print url+pth
##    else:
##        break


##import urllib2
##import urlparse
##from BeautifulSoup import BeautifulSoup
##
##def getAllUrl(url):
##    try:
##        page = urllib2.urlopen( url ).read()
##    except:
##        return []
##    urlList = []
##    try:
##        soup = BeautifulSoup(page)
##        soup.prettify()
##        for anchor in soup.findAll('a', href=True):
##            if not 'http://' in anchor['href']:
##                if urlparse.urljoin(url, anchor['href']) not in urlList:
##                    urlList.append(urlparse.urljoin(url, anchor['href']))
##            else:
##                if anchor['href'] not in urlList:
##                    urlList.append(anchor['href'])
##
##        length = len(urlList)
##
##        return urlList
##    except urllib2.HTTPError, e:
##        print e
##
##def listAllUrl(urls):
##    for x in urls:
##        print x
##        urls.remove(x)
##        urls_tmp = getAllUrl(x)
##        for y in urls_tmp:
##            urls.append(y)
##
##
##if __name__ == "__main__":
##    urls = ['https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html']
##    while(urls.count>0):
##        urls = getAllUrl('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html')
##        listAllUrl(urls)


#Christopher Reeves Web Scraping Tutorial
#simple web spider that returns array of urls. 
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

##import urllib
##from bs4 import BeautifulSoup
##import urlparse
##import mechanize
##
##
### Set the startingpoint for the spider and initialize 
### the a mechanize browser object
##url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html"
##br = mechanize.Browser()
##
### create lists for the urls in que and visited urls
##urls = [url]
##visited = [url]
##
##
### Since the amount of urls in the list is dynamic
###   we just let the spider go until some last url didn't
###   have new ones on the webpage
##while len(urls)>0:
##    try:
##        br.open(urls[0])
##        urls.pop(0)
##        for link in br.links():
##            newurl =  urlparse.urljoin(link.base_url,link.url)
##            print newurl
##            if newurl not in visited and url in newurl:
##                visited.append(newurl)
##                urls.append(newurl)
##                print newurl
##    except:
##        print "error"
##        urls.pop(0)
##       
##print visited


#Christopher Reeves Web Scraping Tutorial
#multithreaded web spider implimentation
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011
##
##import urllib
##import re
##import time
##from threading import Thread
##import mechanize
##import readability
##from bs4 import BeautifulSoup
##from readability.readability import Document
##import urlparse
##
##
##class MultiScrape:
##    visited = []
##    urls = []
##    glob_visited = []
##    depth = 0
##    counter = 0
##    threadlist = []
##    root = ""
##
##    def __init__(self, url, depth):
##       self.glob_visited.append(url)
##       self.depth = depth
##       self.root = url
##   
##    def run(self):
##        while self.counter < self.depth:
##            for w in self.glob_visited:
##                if w not in self.visited:
##                    self.visited.append(w)
##                    self.urls.append(w)
##            self.glob_visited = []       
##            for r in self.urls:
##                try: 
##                    t = Thread(target=self.scrapeStep, args=(r,))
##                    self.threadlist.append(t)
##                    t.start()            
##                except:
##                    nnn = True 
##            for g in self.threadlist:
##                g.join() 
##            self.counter+=1
##        return self.visited  
##
##    def scrapeStep(self,root):
##        result_urls = []
##        br = mechanize.Browser()
##        br.set_handle_robots(False)
##        br.addheaders = [('User-agent', 'Firefox')]
##        try:
##            br.open(root)
##            for link in br.links():
##                newurl =  urlparse.urljoin(link.base_url,link.url)
##                if urlparse.urlparse(link.base_url).hostname.replace("www.","") in self.root:
##                    result_urls.append(newurl)   
##        except:
##            err = True     
##        for res in result_urls:
##            self.glob_visited.append(res)
##            
##    
##
##
##
##
##
##
##def getReadableArticle(url):
##    br = mechanize.Browser()
##    br.set_handle_robots(False)
##    br.addheaders = [('User-agent', 'Firefox')]
##
##    html = br.open(url).read()
##
##    readable_article = Document(html).summary()
##    readable_title = Document(html).short_title()
##
##    soup = BeautifulSoup(readable_article)
##
##    final_article = soup.text
##
##    links = soup.findAll('img', src=True)
##
##    title_article = []
##    title_article.append(final_article)
##    title_article.append(readable_title)
##    return title_article
##
##    
##
##
##
##def dungalo(urls):
##    article_text =getReadableArticle(urls)[0]
##    d[urls] = article_text
##
##        
##
##def getMultiHtml(urlsList,steps):
##
##    for urls1 in urlsList:
##        try:
##            t = Thread(target=scraper, args=(urls1,steps,))
##            threadlist.append(t)
##            t.start()            
##        except:
##            nnn = True
##
##    for g in threadlist:
##        g.join()
##
##url = "http://adbnews.com/area51"
##url1 = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html"
##mysite = MultiScrape(url1,3)
##
##
##print  mysite.run()
f=open("../keys_hackerrank_q.txt","r")
hkey=f.readlines()
f.close()
import re
import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html"
br = mechanize.Browser()
urls = [url]
visited = [url]
k=0
while len(urls)>0:
    try: 
        br.open(urls[0])
        urls.pop(0)    
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url,link.url)
            b1 = urlparse.urlparse(newurl).hostname
            b2 = urlparse.urlparse(newurl).path
            newurl =  "http://"+b1+b2

            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                #print newurl
                k+=1
    except:
        print "error"
        urls.pop(0)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True
c=[]
for i in visited:
    html = urllib.urlopen(i)
    soup = BeautifulSoup(html,"lxml")
    data = soup.findAll(text=True)
    result = filter(visible, data)
##    print i
    if len(result)>2:
        if len(result[2])>10:
            c+=[result[2]]
c=list(set(c))
c.sort()
for i in c:
    print i

reslt=[]
for i in hkey:
    url="https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/"+i.strip()+".json"
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html,"lxml")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    reslt+=[result]
for i in reslt:
    print i
