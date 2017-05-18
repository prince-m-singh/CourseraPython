# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count =0
sum =0
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('class', None)
    print 'Contents:',tag.contents[0]
    print int(tag.contents[0])
    sum=sum+int(tag.contents[0])
    print 'Attrs:',tag.attrs
    count=count+1
   # print count
print count, sum
