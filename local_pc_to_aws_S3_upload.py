#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import boto3




def file_upload_s3():

    s3_bucket = "elk-data-storage"
    s3 = boto3.resource('s3')

    dir_path = []   # dir_path 은 local PC에 업로드 할 경로를 저장하기 위함 용도
    file_name = []  # file_name 은 업로드 할 경로에 파일 이름을 저장하기 위한 용도 

    
    
    
    directory_path = "/home/ubuntu/data"       # ★★★★★ 업로드 할 파일 경로를 지정 ★★★★★
    for file in os.listdir(directory_path):
        path = os.path.join(directory_path,file) # C:\Users\injekim97\Desktop\IAM_USER_ELK+ {파일 이름} 식으로 붙어짐
        dir_path.append(path)      
        file_name.append(file)
        print(path)
        print(dir_path)
        print(file_name)     


    #  ★★★★★ range는 업로드 할 파일에 수에 따라 range(수)를 부여함 ★★★★★
    # e.g : 5개면 5를 부여해야함 0~4 총 5개
    # ★★★★★ 일부로 try , except 문을 사용해서 총 999개의 해당 경로의 파일을 업로드 하게끔 함. ★★★★★
    
    try :
        for i in range(999):
            s3.meta.client.upload_file(dir_path[i], s3_bucket,file_name[i])   
    
    except Exception as e :
        print(e)

    print("Local PC -> AWS S3 파일 업로드를 완료하였습니다.")
    
file_upload_s3()


# In[ ]:




