
## 목적

* 자동화 댓글 작성 

* cafe crawling 

* 발생된 log를 파일형식(log.csv)버전과 DB에 직접 저장 버전 


## Run

* NAS 의 Docker Ubuntu container 를 활용 

* crontab 스케쥴러를 이용하여 30분당 1회 동작하도록 셋팅 
  * crontab 은 shell script로 작성하여 crontab에 등록함

