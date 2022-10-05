
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

driver=webdriver.Chrome('./chromedriver') #크롬 드라이버
# driver.get('https://imjingakcamping.co.kr/resv/res_01.html?checkdate=2022-05-18') #접속할 url (테스트)
driver.get('https://imjingakcamping.co.kr/resv/res_01.html?checkdate=2022-09-09') #접속할 url (실전) 

# 예약 전 유의사항을 확인했습니다
xpath = "//input[@type='checkbox']"
box = driver.find_element_by_xpath(xpath)
driver.execute_script("arguments[0].click()", box) 

# 사이트 선택
#xpath = "//input[@type='checkbox' and @id='ph_a_04']" # 평화: ph_a_{0:D2}, 힐링: hl_{0:D2}
# xpath = "//input[@type='checkbox' and @id='ph_a_14']" # 평화: ph_a_{0:D2}, 힐링: hl_{0:D2}
#xpath = "//input[@type='checkbox' and @id='ph_a_13']" # 평화: ph_a_{0:D2}, 힐링: hl_{0:D2}
#xpath = "//input[@type='checkbox' and @id='ph_a_15']" # 평화: ph_a_{0:D2}, 힐링: hl_{0:D2}
# xpath = "//input[@type='checkbox' and @id='ph_a_10']" # 평화: 10번
xpath = "//input[@type='checkbox' and @id='cv_b_15']" # 카라반B 15번
# xpath = "//input[@type='checkbox' and @id='cv_b_14']" # 카라반B 15번
box = driver.find_element_by_xpath(xpath)
driver.execute_script("arguments[0].click()", box) 

time.sleep(1) 

# 기간
xpath = "//select[@name='night[]']"
select = Select(driver.find_element_by_xpath(xpath))
select.select_by_index(1) # 0: 1박2일, 1: 2박3일 

# 대인
xpath = "//select[@name='mem1[]']"
select = Select(driver.find_element_by_xpath(xpath))
select.select_by_index(2) # n명 

# 소인
xpath = "//select[@name='mem2[]']"
select = Select(driver.find_element_by_xpath(xpath))
select.select_by_index(2) # n명 

# 예약하기
xpath = "//button[@onclick='doReserv();']"
button = driver.find_element_by_xpath(xpath)
button.click() 

time.sleep(1) 

# 예약정보
driver.find_element_by_name('r_name').send_keys('김선화')
driver.find_element_by_name('r_hp').send_keys('01076797933')
driver.find_element_by_name('r_email').send_keys('tlgudlove@naver.com')
driver.find_element_by_name('r_jumin1').send_keys('851206')
driver.find_element_by_name('r_car[]').send_keys('62나6239') 

# 취소 및 환불 규정에 관한 약관을 읽었으며 이에 동의합니다
xpath = "//input[@type='checkbox' and @id='agree_refund']"
box = driver.find_element_by_xpath(xpath)
driver.execute_script("arguments[0].click()", box) 

# 개인정보관리에 관한 약관을 읽었으며 이에 동의합니다
xpath = "//input[@type='checkbox' and @id='agree_privite']"
box = driver.find_element_by_xpath(xpath)
driver.execute_script("arguments[0].click()", box) 

# 상기 이용약관에 동의합니다
xpath = "//input[@type='checkbox' and @id='agree_all']"
box = driver.find_element_by_xpath(xpath)
driver.execute_script("arguments[0].click()", box) 

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 

time.sleep(1) 

# 지역주민할인
xpath = "//input[@type='checkbox']"
box = driver.find_element_by_xpath(xpath)
driver.execute_script("arguments[0].click()", box) 

#time.sleep(1)
#driver.send_keys(Keys.ENTER)