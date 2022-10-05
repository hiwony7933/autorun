
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, random, os, urllib3, csv, json, datetime
import pyperclip

# site url
naver_login_url = "https://nid.naver.com/nidlogin.login"
naver_url = 'https://www.naver.com/'

# file path
log_path = './log/log.csv'
config_path = './config/config.json'

## read config json file 
try : 
    with open(config_path, 'r') as f: 
        config = json.load(f) 
except : 
    print('Check config.json path : ./config/config.json')

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
driver = webdriver.Chrome('./config/chromedriver', chrome_options=options)

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


