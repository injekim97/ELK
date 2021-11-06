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
**2021.11.06 : 가상 머신에서 MySQL 설치 및 실행 방법(외부접속 허용방법)  


*** 
**2021.11.0? :  크롤링 카테고리 만들어서 인턴 때 했던 것들 다 업로드 하기  