import urllib
import re
from BeautifulSoup import *

serviceurl = ('https://book.douban.com/top250?')
num = 25
for page in [0*num,num,2*num,3*num,4*num,5*num,6*num,7*num]:  #pages to iterate
    url = serviceurl + urllib.urlencode({'start':page})       #final url to visit
    print url
    
    uh = urllib.urlopen(url)
    html = uh.read()

    soup = BeautifulSoup(html)



    tags = soup('a') + soup('span')
    alist = []
    comments = []
    for tag in tags:
        line = str(tag)
	title = re.findall('\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s([^><]+)\n\n', line)
	comment = re.findall('class="inq">(.+)<', line)
	
	for element in title:
	    if element != []:
	        element = element.strip('\n')
		alist.append(element)
	
	for element in comment:
	    if element != []:
		comments.append(element)

#    print len(alist)
#    for element in alist:
#        print str(element).decode('string_escape')
#    print len(comments)
#    for element in comments:
#	print str(element).decode('string_escape')

    for i in range(25):
	print str(alist[i]).decode('string_escape'),'----', str(comments[i]).decode('string_escape')
