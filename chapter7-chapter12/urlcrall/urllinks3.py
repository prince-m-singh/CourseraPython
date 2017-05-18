# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

def urlcheck(urllink,position):
   # print urllink,position
    html = urllib.urlopen(urllink).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    i=0
    
    for tag in tags:
        i=i+1
   # print tag.get('href', None)
        if i%int(position) == 0:
            return tag.get('href', None)
            
            
            #print i, j
            #print 'TAG:',tag
            #print 'URL:',tag.get('href', None)
            #print 'Contents:',tag.contents[0]
            
def urltagName(urllink,position):
    html = urllib.urlopen(urllink).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    i=0
    
    for tag in tags:
        i=i+1
   # print tag.get('href', None)
        if i%int(position) == 0:
            return tag.contents[0]
    

url = raw_input('Enter - ')
count=raw_input('Enter count: ')
position=raw_input('Enter position: ')
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
for i in range(0,int(count)):
    #print type(url)
    #print type(str(urlcheck(url,position)))
    print urltagName(url,position), urlcheck(url,position)
    url=str(urlcheck(url,position))
    #print url
