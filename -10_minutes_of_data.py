#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import requests
import datetime # 현재 시간을 가져오기 위한 모듈
import time
import pymysql






serial_arrlist = [
"24:0A:C4:22:40:7E",
"24:6F:28:3C:77:46",
"24:0A:C4:22:34:FA",
"24:0A:C4:22:37:72", # unv_0001
"24:0A:C4:22:41:B6",
"24:0A:C4:22:37:D2",
"24:0A:C4:22:41:C2",
"24:0A:C4:22:34:2E",
"24:0A:C4:22:39:12",
"24:0A:C4:22:37:9E",
"24:0A:C4:22:38:EA",
"24:0A:C4:22:41:6A",
"24:0A:C4:22:3E:9A",
"24:0A:C4:22:34:B2",
"24:6F:28:3C:7A:22",
"24:0A:C4:22:43:1A",
"24:0A:C4:22:3A:AE",
"24:0A:C4:22:35:B6",
"24:0A:C4:22:44:3E",
"24:0A:C4:22:36:66",
"24:0A:C4:22:34:0A",
"24:0A:C4:22:34:8E",
"24:0A:C4:22:3D:0A",
"24:0A:C4:22:42:4A",
"24:6F:28:3C:7D:7A",  # org_0001
"24:0A:C4:22:34:FA", # COM_0001
"24:6F:28:3C:77:46", # COM_0001
]





# Azure or AWS DB 연동
def get_db():
    db = pymysql.connect(
        host='mysql.monorama.kr',
        port=3306,
        user='admin',
        passwd='1/zw;GytAwx*',
        db='AIR',
        charset='utf8'
    )
    return db









# todate를 위한 함수.(현재시간에서 10분 추가)
def ten_minute_add():
    now_time = datetime.datetime.now()
    now_plus_10 = now_time + datetime.timedelta(minutes = 10)
    now_plus_10 = now_plus_10.strftime('%Y%m%d%H%M%S')
    #print(now_plus_10)

    return now_plus_10





# fromdate를 위한 함수 (현재시간에서 10분 감소)
def ten_minute_minus():
    now_time = datetime.datetime.now()
    now_minus_10 = now_time - datetime.timedelta(minutes = 45)
    now_minus_10 = now_minus_10.strftime('%Y%m%d%H%M%S')
    #print(now_minus_10)

    return now_minus_10








#  org json 데이터
my_dict = {}  # ★★★ java에서는 map (Hash table, Hash map) , Python 에서는 dict(사전) 사용, 같은기능임 ★★★

def sc_org_json_data():
    db = get_db()
    mycursor = db.cursor()


    # -------------------postman query data -----------------------------
    url = "https://us-central1-mytypescript-62c14.cloudfunctions.net/getData"

    try :
        for i in range(0,len(serial_arrlist)):


            # ------------------ 계속 돌리기 위해 추가 및 수정한 부분----------------------
            my_dict[serial_arrlist[i]] = ten_minute_minus() # ★★★★★ dict 함수에 동시에 key & value 넣음 ★★★★★

            print("현재 작업중인 시리얼 넘버:", serial_arrlist[i])

            fromDate = my_dict[serial_arrlist[i]]   # dict 시리얼 넘버(key)에 저장된 현재시간(value) - 0분을 저장. 111번 라인 
            toDate = ten_minute_add()  # ten_minute_add()을 사용해서, currnet_time (현재시간) 에서 10분을 추가해서 저장 
            
            print("fromDate: ",fromDate) # 20210815210000
            print("toDate: ",toDate)   # 20210815211000
            



            # --------------------------------POSTMAN 그대로 가져옴-----------------------------
            payload = json.dumps({
                "fromDate": fromDate,        # 이전에 수행되었던 시간
                "toDate": toDate,      # 현재시간(20210811154000) - 이전에 수행되엇던 시간(20210811153500) = 이번차례에 수행되는 시간
                "siteCode": "com_0001",
                "key": "Qkslffk@91",
                "serialNum" : serial_arrlist[i],
                "format": "json",
                "segment": "avg"
            })

            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            data = response.json()
            print(data) # {'message': 'Not Found', 'content': 'Plz, check condition'}


            # ------------------ 계속 돌리기 위해 추가 및 수정한 부분 2 ----------------------
            my_dict[serial_arrlist[i]] = toDate # ★★★★★ 작업이 끝난 후, 각 시리얼 넘버에 toDate를 넣어줌, 그래야 시간이 지난 것에 대해 데이터가 들어감 ★★★★★
            #print(my_dict)



            try :
                for i in data:
                    # data 값이 비어 있으면, message, content 라는 str 값이 data에 존재함.
                    # 그렇기 때문에, 에러메세지(string indices must be integers)가 발생함
                    # 데이터가 제대로 들어오면 에러가 발생하지 않음
                    #print(i) # 위에 주석으로 적어 놓았음

                    mycursor.execute("insert into hanbang_air_data(SerialNum,Co2,Humid,Pm10,Pm5,Temp,Vocs,timeZone,ReportTime,Lat,Lng) values (%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(i["serialNum"],i["co2"],i["humid"],i["pm10"],i["pm5"],i["temp"],i["vocs"],i["timeZone"],i["reportTime"],i["lat"],i["long"]))

                db.commit()
                db.close()

                print("=======성공적으로 json data 삽입을 완료하였습니다.=====")
                print("\n\n\n")


            except Exception as e:
                print("DB에 JSON 데이터 삽입 실패:",e)
                print("\n\n\n")


    except :
        pass
    
    

    


#  unv json 데이터
my_dict2 = {}  # ★★★ java에서는 map (Hash table, Hash map) , Python 에서는 dict(사전) 사용, 같은기능임 ★★★

def sc_unv_json_data():
    db = get_db()
    mycursor = db.cursor()


    # -------------------postman query data -----------------------------
    url = "https://us-central1-mytypescript-62c14.cloudfunctions.net/getData"

    try :
        for i in range(0,len(serial_arrlist)):


            # ------------------ 계속 돌리기 위해 추가 및 수정한 부분----------------------
            my_dict2[serial_arrlist[i]] = ten_minute_minus() # ★★★★★ dict 함수에 동시에 key & value 넣음 ★★★★★

            print("현재 작업중인 시리얼 넘버:", serial_arrlist[i])

            fromDate = my_dict2[serial_arrlist[i]]   # dict 시리얼 넘버(key)에 저장된 현재시간(value) -10분을 저장. 111번 라인 
            toDate = ten_minute_add()  # ten_minute_add()을 사용해서, currnet_time (현재시간) 에서 10분을 추가해서 저장 
            
            print("fromDate: ",fromDate) # 20210815210000
            print("toDate: ",toDate)   # 20210815211000
            



            # --------------------------------POSTMAN 그대로 가져옴-----------------------------
            payload = json.dumps({
                "fromDate": fromDate,        # 이전에 수행되었던 시간
                "toDate": toDate,      # 현재시간(20210811154000) - 이전에 수행되엇던 시간(20210811153500) = 이번차례에 수행되는 시간
                "siteCode": "unv_0001",
                "key": "Qkslffk@91",
                "serialNum" : serial_arrlist[i],
                "format": "json",
                "segment": "avg"
            })

            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            data = response.json()
            print(data) # {'message': 'Not Found', 'content': 'Plz, check condition'}


            # ------------------ 계속 돌리기 위해 추가 및 수정한 부분 2 ----------------------
            my_dict2[serial_arrlist[i]] = toDate # ★★★★★ 작업이 끝난 후, 각 시리얼 넘버에 toDate를 넣어줌, 그래야 시간이 지난 것에 대해 데이터가 들어감 ★★★★★
            #print(my_dict)



            try :
                for i in data:
                    # data 값이 비어 있으면, message, content 라는 str 값이 data에 존재함.
                    # 그렇기 때문에, 에러메세지(string indices must be integers)가 발생함
                    # 데이터가 제대로 들어오면 에러가 발생하지 않음
                    #print(i) # 위에 주석으로 적어 놓았음

                    mycursor.execute("insert into hanbang_air_data(SerialNum,Co2,Humid,Pm10,Pm5,Temp,Vocs,timeZone,ReportTime,Lat,Lng) values (%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(i["serialNum"],i["co2"],i["humid"],i["pm10"],i["pm5"],i["temp"],i["vocs"],i["timeZone"],i["reportTime"],i["lat"],i["long"]))

                db.commit()
                db.close()

                print("=======성공적으로 json data 삽입을 완료하였습니다.=====")
                print("\n\n\n")


            except Exception as e:
                print("DB에 JSON 데이터 삽입 실패:",e)
                print("\n\n\n")


    except :
        pass
    
    
    


#  com json 데이터
my_dict3 = {}  # ★★★ java에서는 map (Hash table, Hash map) , Python 에서는 dict(사전) 사용, 같은기능임 ★★★

def sc_com_json_data():
    db = get_db()
    mycursor = db.cursor()


    # -------------------postman query data -----------------------------
    url = "https://us-central1-mytypescript-62c14.cloudfunctions.net/getData"

    try :
        for i in range(0,len(serial_arrlist)):


            # ------------------ 계속 돌리기 위해 추가 및 수정한 부분----------------------
            my_dict3[serial_arrlist[i]] = ten_minute_minus() # ★★★★★ dict 함수에 동시에 key & value 넣음 ★★★★★

            print("현재 작업중인 시리얼 넘버:", serial_arrlist[i])

            fromDate = my_dict3[serial_arrlist[i]]   # dict 시리얼 넘버(key)에 저장된 현재시간(value) - 10분을 저장. 111번 라인 
            toDate = ten_minute_add()  # ten_minute_add()을 사용해서, currnet_time (현재시간) 에서 10분을 추가해서 저장 
            
            print("fromDate: ",fromDate) # 20210815210000
            print("toDate: ",toDate)   # 20210815211000
            



            # --------------------------------POSTMAN 그대로 가져옴-----------------------------
            payload = json.dumps({
                "fromDate": fromDate,        # 이전에 수행되었던 시간
                "toDate": toDate,      # 현재시간(20210811154000) - 이전에 수행되엇던 시간(20210811153500) = 이번차례에 수행되는 시간
                "siteCode": "com_0001",
                "key": "Qkslffk@91",
                "serialNum" : serial_arrlist[i],
                "format": "json",
                "segment": "avg"
            })

            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            data = response.json()
            print(data) # {'message': 'Not Found', 'content': 'Plz, check condition'}


            # ------------------ 계속 돌리기 위해 추가 및 수정한 부분 2 ----------------------
            my_dict3[serial_arrlist[i]] = toDate # ★★★★★ 작업이 끝난 후, 각 시리얼 넘버에 toDate를 넣어줌, 그래야 시간이 지난 것에 대해 데이터가 들어감 ★★★★★
            #print(my_dict)



            try :
                for i in data:
                    # data 값이 비어 있으면, message, content 라는 str 값이 data에 존재함.
                    # 그렇기 때문에, 에러메세지(string indices must be integers)가 발생함
                    # 데이터가 제대로 들어오면 에러가 발생하지 않음
                    #print(i) # 위에 주석으로 적어 놓았음

                    mycursor.execute("insert into hanbang_air_data(SerialNum,Co2,Humid,Pm10,Pm5,Temp,Vocs,timeZone,ReportTime,Lat,Lng) values (%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(i["serialNum"],i["co2"],i["humid"],i["pm10"],i["pm5"],i["temp"],i["vocs"],i["timeZone"],i["reportTime"],i["lat"],i["long"]))

                db.commit()
                db.close()

                print("=======성공적으로 json data 삽입을 완료하였습니다.=====")
                print("\n\n\n")


            except Exception as e:
                print("DB에 JSON 데이터 삽입 실패:",e)
                print("\n\n\n")


    except :
        pass
    
            
#-------------------------------main----------------------------
while True :
    print("=========현재 작업 중인 SiteCode:  org_0001  ==========")
    sc_org_json_data()
    print("============org_0001 작업이 끝났습니다. =============")
    time.sleep(10)
    
    
    print("===============새로운 작업을 시작합니다 ====================")
    print("==========현재 작업 중인 SiteCode:  unv_0001  ==========")
    sc_unv_json_data()
    print("============unv_0001 작업이 끝났습니다. =============")
    time.sleep(10)

    
    print("===============새로운 작업 시작============")
    print("=========현재 작업 중인 SiteCode: COM_0001 =========")
    sc_com_json_data()
    print("===========COM_0001 작업 종료=============")
    time.sleep(10)
    
    
    print("========= org,unv,com 작업  1 cycle success!! ==========")
    print("\n\n\n")
    
# In[ ]:


# In[ ]:





# In[ ]:




