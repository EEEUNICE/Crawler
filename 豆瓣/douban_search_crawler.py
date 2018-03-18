# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 00:09:36 2018

@author: CAS015
"""

import requests
from bs4 import BeautifulSoup
import time
import json,xlrd
import random,string,codecs


def getjson(name):
  try:
    head = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    "Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11)),
    'Connection':'close'
}
    requests.adapters.DEFAULT_RETRIES = 5#增加重试连接次数
  #  proxy = {'http': '27.36.116.226	:3128'}  
    s = requests.session()
    s.keep_alive = False
    res=requests.get('http://api.douban.com//v2/movie/search?q=%s'%name,headers=head)#,proxies=proxy)  #以GET方式向网站发送请求，返回网站响应
    soup=BeautifulSoup(res.text,"lxml")  #将非结构化数据结构化
    
#    print(soup) 
    data=json.loads(soup.select('p')[0].string)
    details=str(data['subjects'][0])
    fp = codecs.open("details.json","a","utf-8")
    fp.write(details)
    fp.close()
    print(name)
#    time.sleep(10)
  except TypeError:
        print('TypeError',name)
  except IndexError:
       print('查找不到',name)    
  except KeyError:
       print('无法连接',name) 



data = xlrd.open_workbook(r'C:\Users\CAS015\Desktop\B题\节目一览.xlsx')
table = data.sheets()[0]
nrows = table.nrows #行数
ncols = table.ncols #列数
#for i in range(0,nrows):
for i in range(1158,nrows):
    values=table.row_values(i)
    for item in values:    
#        if i%50==0:
#            time.sleep(300)
            
        getjson(item)
        
