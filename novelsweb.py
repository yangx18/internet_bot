from typing import Optional

import requests
import os
import re
from multiprocessing.dummy import Pool

def Getcontext_Save(list):
    '''
    grab the chapter context
    '''
    title = list[0]
    chapter_number = list[1]
    url = list[2]

    htm = requests.get(url).content
    received = htm.decode('gbk')
    context = re.findall('<p>(.*?)</p>',received,re.S)[0]
    context = context.replace('<br />','')

    os.makedirs(title,exist_ok=True)### Create dirs if not exist
    with open(os.path.join(title,chapter_number+'.txt'),'w',encoding='utf-8') as f:
        f.write(context)


### Request the novel web
html = requests.get('https://www.kanunu8.com/book3/6879/').content
html = html.decode('gb2312','ignore')

### Get the content
large_range_content = re.search('首页(.*?第十章)</a></td>',html,re.S).group(1)
### Get book title
Book_title =  re.findall('<h1><strong><font color="#dc143c">(.*?) </font></strong></h1></td>',large_range_content,re.S)[0]

url_list = {} # dic store the url for every chapter
chapter_list = re.findall('a href="(131.*?)">',large_range_content,re.S)
a = 1 # count for each chapter

###Grab url for every chapter and store in the dic
for each in chapter_list:
    url_list['Chapter'+str(a)] = 'https://www.kanunu8.com/book3/6879/' + each
    a = a+1
### store Book'title, chapter number and url into lis t for using the multiple processing
List = [ ]

for key,value in url_list.items():
    List.append([Book_title,key,value])

pool = Pool(3)
pool.map(Getcontext_Save,List)

