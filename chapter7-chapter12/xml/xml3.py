import urllib
import xml.etree.ElementTree as ET
url = raw_input('Enter location: ')
data = urllib.urlopen(url).read()
print 'Retrieving', url
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
print "Data  Operation"
print type(tree)
results = tree.findall('comments/comment')
len=len(results)
#res=tree.find('comments').find('coment').find('name').text
print "Count: " ,len
#print results, len
sum=0
for item in results:
    #print 'Count tag', item.find('count').text
    num=item.find('count').text
    sum=sum+ int (num)
    #print sum
print sum