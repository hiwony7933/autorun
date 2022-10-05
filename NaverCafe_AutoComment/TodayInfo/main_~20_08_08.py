
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs 
import pandas as pd 
import numpy as np
import time, random, os, urllib3, csv, json, datetime
import urllib.request

# site url
naver_login_url = "https://nid.naver.com/nidlogin.login"
naver_url = 'https://www.naver.com/'

# file path
log_path = './log.csv'
config_path = './config.json'
file_path = './file_csv/'

## read config json file 
try : 
    with open(config_path, 'r') as f: 
        config = json.load(f) 
except : 
    print('Check config.json path : ./config.json')

# User info
userid = config['USERINFO']["USERNAME"]
userpw = config['USERINFO']["PASSWORD"]
target_url = config['USERINFO']["URL"]

# now time
now_time = str(datetime.datetime.now())

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
options.add_argument("lang=ko_KR") # 한국어!
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

# list index find
def find_index(data, target):
    res = []
    lis = data
    while True:
        try:
            res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
            lis = data[res[-1]+1:]
        except:
            break     
    return res

def naver_login_2(id, pw) :
    driver.get(naver_login_url)
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1,2))
    
    driver.execute_script("document.getElementsByName('id')[0].value = \'" + id + "\'")
    time.sleep(random.uniform(1,2))
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    time.sleep(random.uniform(1,2))
    driver.find_element_by_css_selector('.btn_global').click()
    time.sleep(random.uniform(1,2))

    naver_home = driver.current_url # 현재 주소 가져오기
    driver.implicitly_wait(10)
    
    if naver_home == naver_url :         
        print(now_time,'login_complete')
    else :
        print(now_time,'login_failed')
        driver.quit()   

naver_login_2(userid, userpw)

try :
    with open(log_path, 'r', encoding='utf-8') as f :
        rdr = csv.reader(f)
        line =[]
        for imsi in rdr:
            line.append(imsi[1])
        print('list up complete')
except :
    print('Check list.csv path : ./log.csv')

def page_scroll(page_down) :
    for j in range(1, page_down) :        
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(random.uniform(0.7,0.8))


#367번에서 에러 발생함 6월달꺼
for i in range(367, 1143) :
    oso_url = 'https://m.cafe.naver.com/ca-fe/web/cafes/16105095/menus/921'
    driver.get(oso_url)
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1,3))
    body = driver.find_element_by_tag_name('body')  # 스크롤하기 위해 소스 추출

    page_down = ((i // 52) * 2)
    print(page_down, 'page_down')
    if page_down > 13 :
        page_scroll(15)
    else :
        page_scroll(page_down)

    for j in range(13, page_down) :        
        driver.find_element_by_xpath('//*[@id="ct"]/div/div/div/a').click()  # 스크롤 14번 내리고부터는  더보기    
        time.sleep(random.uniform(0.7,0.8))
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(random.uniform(0.7,0.8))

    page_soup = bs(driver.page_source, 'html.parser')
    tit = page_soup.select('#ct > div > div > ul > li:nth-child(' + str(i) + ')')[0].get_text()
    
    if tit.find('오소텍스트') > 0 :
        print(i)
        
        #에러 발생지점 엘리먼트를 찾을수없다고함.
        driver.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li[' + str(i) + ']').click()   


        time.sleep(random.uniform(2,3))
        # //*[@id="ct"]/div/div/ul/li[376]/div/a[1]/strong
        result = driver.current_url 
        comment_board_numbers = result.split('articles/')[1] # 글 번호 분리
        comment_board_numbers = comment_board_numbers.split('?fromList')[0] # 글 번호 분리
        find_index_ = find_index(line, comment_board_numbers)

        if not find_index_ : 
            with open(log_path, 'a', encoding='utf-8', newline='') as fs :
                soup = bs(driver.page_source, 'html.parser')

                # 제목
                title = soup.select('#ct > div:nth-child(1) > div > h2')[0].get_text() 
                print(title)

                # 파일명
                datetime = soup.select('span.date')[0].get_text().split('작성일')[1]
                date = datetime[:10]
                date = date.replace('.','_')
                file_name = str(date) + '.csv'
                print(file_name)

                # 내용 ~ 2020_08_07
                con = soup.select('#postContent')[0].select('p')
                con_len = len(con)
                content_li = []
                for k in range(con_len) :
                    content_li.append(con[k])

                data = pd.DataFrame(content_li[0])
                con_len = len(content_li)

                for u in range(1, con_len) :
                    u = pd.DataFrame(content_li[u])
                    data_result = pd.concat([data,u])

                data_result.to_csv(file_path + file_name, 'w')
                dataset = pd.read_csv(file_path + file_name,'w')
                redata = dataset['0'].replace('<br/>', np.nan )
                redata = redata.dropna(how='any', axis=0)
                redata.to_csv(file_path + file_name, 'w', index=False)            

                wr = csv.writer(fs)
                wr.writerow([now_time, comment_board_numbers, userid, 'complete', str(i), file_name])
                print(now_time, comment_board_numbers, 'complete', str(i))
        else :
            print(now_time, comment_board_numbers, 'already', str(i))
            time.sleep(random.uniform(2,3))
            
    else :
        continue
# except : 
#     print("Exception PASS")
#     pass
