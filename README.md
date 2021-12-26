# ELK(Elasticsearch, Logstash, Kibana)
ELK 기초 개념 부터 설치 및 데이터 분석 하는 방법까지 업로드 할 리포지토리   

#### ELK Stack(Elasticsearch, Logstash, Kibana)
Elasticsearch   
-> Logstash로부터 받은 데이터를 검색 및 집계를 하여 필요한 관심 있는 정보를 획득

Logstash     
-> 다양한 소스( DB, csv파일 등 )의 로그 또는 트랜잭션 데이터를 수집, 집계, 파싱하여 Elasticsearch로 전달

Kibana    
-> Elasticsearch의 빠른 검색을 통해 데이터를 시각화 및 모니터링
 
*** 
**2021.10.25 : PC에서 ELK 설치 방법**  
1.  https://www.elastic.co/kr/downloads/elasticsearch  WINDOWS 파일 받은 후, 압축 풀기
2.  https://www.elastic.co/kr/downloads/logstash   WINDOWS 파일 받은 후, 압축 풀기
3.  https://www.elastic.co/kr/downloads/kibana  WINDOWS 파일 받은 후, 압축 풀기
4.  시스템 -> 관련 설정(고급 시스템 설정) -> 고급 -> 환경변수(맨 밑) 클릭  -> 시스템 변수에 있는 path를 더블 클릭 -> 새로 만들기를 눌러 logstash 경로를 넣어준 후, 차례대로 kibana , elasticsearch경로를 각 각 넣어줌 **(사진 첨부)**
6.  cmd -> 관리자 명령프롬포트를 켜서 bin/elasticsearch.bat 실행
7.  kibana/config/kibana.yml (port:5601) 유지 및 bin/kibana.bat 실행
8.  bin/logstash -> logstash.bat 메모장을 열어 set JAVA_HOME=C:\ElasticSearch\logstash-7.11.2\jdk 추가 후 저장
9.  \bin>logstash -f logstash.conf 으로 logstash 실행

*** 
**2021.10.29 : logstash - MySQL 연동 및 실행 방법(jdbc input plugin)**     
1-1. mysql-connector-java-8.0.23 을 다운 후 압축을 풀어준다. (Linux or window)    
1-2. logstash.conf 파일을 ./logstash -f logstash.conf 로 실행할 수 있다.  

**2021.10.29 : apache-log를 kibana를 이용하여, geoip**    
-> apache-log conf file upload (아파치 로그 파일을 kibana에서 geoip를 찍을 수 있음)  

**2021.10.29 : Linux 에서 ELK 설치 및 실행 방법(ELK install guide file (ubuntu18.04))**    

*** 
**2021.11.06 : 가상 머신에서 MySQL 설치 및 실행 방법(외부접속 허용방법)**     


*** 
**2021.11.16 : 로컬PC에 있는 CSV 파일 데이터를 elasticsearch에 전송하는 방법**    
-> PC(CSV file) to Elasticsearch.conf file    


*** 
**2021.11.26 : Python 언어로 logstash 에 사용될 다중 테이블을 넣는 코드 작성**   
-> jdbc_multi_table_insert   


***  
**2021.11.27 : ELK install (Ubuntu20.04) + XPack(Security 설정 및 User Create) + jdbc on Azure**    
-> ELK install (Ubuntu20.04) + XPack   


*** 
**2021.12.19 :  JSON DATA를 MySQL DB에 저장하는 방법**     
-> 파일명 : PC에 json 파일을 DB에 저장하는 방법   


*** 
**2021.12.25 : How to run Background in elasticsearch & kibana?**   
-> 파일명 : elasticsearch & kibana background run.txt      


*** 
**2021.12.26 : How to display latitude and longitude on the map using Logstash?**   
-> 파일명 : geopoint(Lat,Long).conf  
-> DB에 저장된 데이터를 kibana에 위도와 경도(좌표)를 나타내기 위한 conf 파일   




*** 
**2021.12.27 : How to store a large-capacity CSV in the DB?**   
-> 파일명 : Large_CSV(DATA SAVE Method).txt   
-> 리눅스에서 CSV로 저장된 10만 컬럼이상 데이터들을 DB에 저장하는 방법   

