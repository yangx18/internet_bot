import requests
import time
from multiprocessing.dummy import Pool


#request url web method
def query(url):
    requests.get(url)


start = time.time()#count for time

#request google web 100 times
for i in range(100):
    query('http://www.google.com')

end = time.time()#end time

print('time for signle: %f' % (end - start))
'''
multiplprocessing for requring web
'''
start = time.time()

url_list = ['http://www.google.com']*100
pool = Pool(5)
pool.map(query,url_list)
end = time.time()
print('time for multipl : %f'%(end - start))
