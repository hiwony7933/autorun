from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, os, urllib3, json, requests, ast
from selenium.webdriver.chrome.options import Options

random_sl = random.uniform(3,5)

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('no-sandbox')
# options.add_argument('disable-dev-shm-usage')
# options.add_argument('--disable-gpu')
# driver = webdriver.Chrome('innaver/chromedriver', chrome_options=options)

driver = webdriver.Chrome('innaver/chromedriver')

login_url = "https://nid.naver.com/nidlogin.login"
nuc_url ='https://cafe.naver.com/northpeakuser'
kan_url ='https://cafe.naver.com/campingkan' 

userid = 'tlgudlove'
userpw = 'tlgud063'

driver.get(login_url)
driver.implicitly_wait(10)
time.sleep(random_sl)

# login 한글자씩
for i in range(len(userid)) :
    random_id = random.uniform(0,1)
    driver.find_element_by_xpath('//*[@id="id"]').send_keys(userid[i])
    time.sleep(random_id)

time.sleep(random_sl)

for i in range(len(userpw)) :
    random_pw = random.uniform(0,1)
    driver.find_element_by_xpath('//*[@id="pw"]').send_keys(userpw[i])
    time.sleep(random_pw)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
driver.implicitly_wait(10)
print('login commplete')



time.sleep(random_sl)

driver.get(nuc_url)
driver.implicitly_wait(10)
time.sleep(random_sl)
driver.find_element_by_xpath('//*[@id="menuLink0"]').click()
driver.implicitly_wait(10)
print('NUC join')

time.sleep(random_sl)

driver.get(kan_url)
driver.implicitly_wait(10)
time.sleep(random_sl)
driver.find_element_by_xpath('//*[@id="menuLink0"]').click()
driver.implicitly_wait(10)
print('Kan join')

time.sleep(5)
driver.quit()

