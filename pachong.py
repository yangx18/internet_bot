import re
import csv
'''
with open('.txt','r/w',encoding='') as f:
    xxx = f.read()
爬本地文件
with open('.csv','w',encoding='') as f 
    write = csv.DictWriter(f,filenames = [])
    writer = writeheader()
    writer = writerows({.....})
'''
with open('tieba.txt','r',encoding='UTF-8') as f:
    source = f.read()

result_list=[]
every_reply = re.findall(' <a data-field=(.*?)class="j_lzl_container core_reply_wrapper hideLzl" ',source,re.S)

for each in every_reply:
    namerow = re.findall('class="p_author_name j_user_card"(.*?)class=',each,re.S)
    result={}
    result['username'] = re.findall('target="_blank">(.*?)<img',namerow[0],re.S)
    result['content'] = re.findall('class="d_post_content j_d_post_content " style="display:;">(.*?)<br>',each,re.S)[0]
    result['date'] = re.findall('<span class="tail-info">(2019.*?)</span>',each,re.S)[0]
    result_list.append(result)

with open('tieba.csv','w',encoding='UTF-8') as f:
    writer = csv.DictWriter(f,fieldnames=['username','content','date'])
    writer.writeheader()
    writer.writerows(result_list)