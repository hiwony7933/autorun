from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random,pyperclip


# 클립보드에 input을 복사한 뒤 해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def copy_input(xpath, userinfo):
    pyperclip.copy(userinfo)
    driver.find_element_by_xpath(xpath).click()
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # win linux
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # mac
    time.sleep(random.uniform(0,3))

def naver_log_in(id, pw) :
    driver.get(naver_login_url)
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1,2))
    
    copy_input('//*[@id="id"]', id)
    time.sleep(random.uniform(1,2))
    
    copy_input('//*[@id="pw"]', pw)
    time.sleep(random.uniform(1,2))

    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(3)

    naver_home = driver.current_url # 현재 주소 가져오기
    driver.implicitly_wait(10)
    
    if naver_home == naver_url :         
        print(now_time,'login_complete')
    else :
        print(now_time,'login_failed')
        driver.quit()   

