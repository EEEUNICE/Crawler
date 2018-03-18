# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 00:27:16 2018

@author: CAS015
"""
import requests
from bs4 import BeautifulSoup
import time
import json
import random,string,codecs


def getjson(id):
  try:
    head={"Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))}
    res=requests.get('https://movie.douban.com/j/subject_abstract?subject_id=%s'%id,headers=head)  #以GET方式向网站发送请求，返回网站响应
    soup=BeautifulSoup(res.text,"lxml")  #将非结构化数据结构化
    time.sleep(5)
    data=soup.select('p')[0].string
    fp = codecs.open("tv-recommend.json","a","utf-8")
    fp.write(data)
    fp.close()
  except TypeError:
        print('TypeError',id)
  except IndexError:
       print('IndexError',id)
head={"Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))}
for j in range(480,40000,20):
#    print('https://movie.douban.com/j/search_subjects?type=tv&tag=%%E7%%83%%AD%%E9%%97%%A8&sort=rank&page_limit=20&page_start=%s'%j)
    res=requests.get('https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start=%s'%j,headers=head) 
    soup=BeautifulSoup(res.text,"lxml")  #将非结构化数据结构化
    dic= json.loads(soup.select('p')[0].string)
    print(j)
    time.sleep(5)
    for i in range(0,20):
        id=dic['subjects'][i]['id']  
        print(id)
        getjson(id)

