# ELK(Elasticsearch, Logstash, Kibana)
ELK 기초 개념 부터 설치 및 데이터 분석 하는 방법까지 업로드 할 리포지토리   


# ELK Concept(Elasticsearch, Logstash, Kibana)
Elasticsearch란?   
-> 텍스트, 숫자, 위치 기반 정보, 정형 및 비정형 데이터 등 모든 유형의 데이터를 위한 분산형 오픈 소스 검색 및 분석 엔진임.  
-> 또한 데이터 수집, 보강, 저장, 분석, 시각화를 위한 오픈 소스 도구 모음인 Elastic Stack의 중심 구성 요소


Logstash란?  
-> 실시간 파이프라인 기능을 가진 오픈소스 데이터 수집 엔진이며, 서로 다른 소스의 데이터를 탄력적으로 통합하고 사용자가 선택한 목적지로 데이터를 정규화할 수 있게 해줌

 

Kibana란?   
-> Elasticsearch에서 색인된 데이터를 검색하고 시각화하는 기능을 제공하며, Elastic Stack 클러스터를 모니터링, 관리 및 보호하기 위한 사용자 인터페이스의 역할과 Elastic Stack에서 개발된 기본 제공 솔루션의 중앙 집중식 허브 역할도 제공함.

 
 

ELK 스택이란? 

Elasticsearch   
-> Logstash로부터 받은 데이터를 검색 및 집계를 하여 필요한 관심 있는 정보를 획득

 

Logstash     
-> 다양한 소스( DB, csv파일 등 )의 로그 또는 트랜잭션 데이터를 수집, 집계, 파싱하여 Elasticsearch로 전달

 

Kibana    
-> Elasticsearch의 빠른 검색을 통해 데이터를 시각화 및 모니터링


*** 
* 2021.10.25  
-> PC에서 ELK 설치 방법



