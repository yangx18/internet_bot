import requests
import re
import csv
'''
用 request 进行网页爬虫
'''

##html = requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode() #request.get('url').content.decode()
###print(html)
html = requests.get('https://tieba.baidu.com/p/6217500017').content.decode()

result_list=[]
every_reply = re.findall(' <a data-field=(.*?)class="j_lzl_container core_reply_wrapper hideLzl" ',html,re.S)
replyuser = []
for each in every_reply:
    namerow = re.findall('class="p_author_name j_user_card"(.*?)class=',each,re.S)
    result={}
    result['username'] = re.findall('target="_blank">(.*?)<img',namerow[0],re.S)
    try:
        replyuser.append(result['username'][0])
    except:
        None
    if result['username']!= replyuser[0] :
        result['content'] = re.findall('class="d_post_content j_d_post_content " style="display:;">(.*?)</div>', each, re.S)[0]
    else:
        result['content'] = re.findall('class="d_post_content j_d_post_content " style="display:;">(.*?)<br>',each,re.S)[0]
    result['date'] = re.findall('<span class="tail-info">(2019.*?)</span>',each,re.S)[0]
    result_list.append(result)

with open('tieba.csv','w',encoding='UTF-8') as f:
    writer = csv.DictWriter(f,fieldnames=['username','content','date'])
    writer.writeheader()
    writer.writerows(result_list)

with open('tieba.csv','r',encoding='UTF-8') as a:
    source = a.read()

print(source)