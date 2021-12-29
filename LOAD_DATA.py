#!/usr/bin/env python
# coding: utf-8

# In[25]:


# -*- coding: utf-8 -*-
import csv
import json
import time
import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# AWS DB 연동 (AWS - ELK)
def get_db():
    db = pymysql.connect(
        host='ec2-13-125-199-218.ap-northeast-2.compute.amazonaws.com',
        port=3306,
        user='admin',
        passwd='1/zw;GytAwx*',
        db='TEST',
        charset='utf8',
        #local_infile=True
        local_infile=1
    )
    return db




# AWS Inquiry TABLE DB에 데이터 넣기
def insert_LOAD_DATA():
    db = get_db()
    mycursor = db.cursor()

    try:
        query = 'LOAD DATA LOCAL INFILE "/home/ubuntu/data/air_quality.csv" INTO TABLE TEST.air_quality FIELDS TERMINATED BY "," IGNORE 1 LINES'
        mycursor.execute(query)
        print("DB에 LOAD DATA 성공")
        db.commit()
        db.close()

    except Exception as e:
        print('db insert inquiry error',e)
        db.close()



# ----------------------- main ------------------------------
insert_LOAD_DATA()


# In[ ]:




