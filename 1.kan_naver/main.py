from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time, random, json, datetime, csv, os, sys
import pyperclip

# site url
naver_login_url = "https://nid.naver.com/nidlogin.login"
naver_url = 'https://www.naver.com/'

# file path
log_path = './log.csv'
config_path = './config.json'
comment_path = './comment.csv'

# 시스템 플랫폼 확인
is_mac = sys.platform == 'darwin'
copy_key = Keys.COMMAND if is_mac else Keys.CONTROL

# 로깅 함수
def log_message(message, error=False):
    timestamp = str(datetime.datetime.now())
    print(f"[{timestamp}] {'ERROR: ' if error else ''}{message}")

# 설정 파일 검증
def validate_config(config):
    required_fields = ['USERNAME', 'PASSWORD', 'URL']
    for field in required_fields:
        if field not in config['USERINFO'] or not config['USERINFO'][field]:
            log_message(f"Missing required field in config: {field}", error=True)
            return False
    return True

## read config json file 
try: 
    with open(config_path, 'r') as f: 
        config = json.load(f)
    if not validate_config(config):
        sys.exit(1)
except Exception as e: 
    log_message(f"Error reading config.json: {str(e)}", error=True)
    sys.exit(1)

# User info
userid = config['USERINFO']["USERNAME"]
userpw = config['USERINFO']["PASSWORD"]
target_url = config['USERINFO']["URL"]

# now time
now_time = str(datetime.datetime.now())

# driver options
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("--disable-gpu")
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

# random comment
def content_comment():
    with open('./comment.csv', 'r', encoding='utf-8') as f:
        imsi_comment = csv.reader(f)
        comment_list = []
        for i in imsi_comment:
            comment_list.append(i[0])
        random_num = random.randint(0, len(comment_list) - 1)
    return comment_list[random_num]

# 요소를 안전하게 찾고 클릭하는 함수
def safe_find_element(by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        log_message(f"Timeout finding element: {value}", error=True)
        return None

def safe_click(element, delay_after=True):
    if element:
        try:
            element.click()
            if delay_after:
                time.sleep(random.uniform(1, 3))
            return True
        except Exception as e:
            log_message(f"Error clicking element: {str(e)}", error=True)
    return False

# 클립보드에 input을 복사한 뒤 해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def copy_input(xpath, input):
    pyperclip.copy(input)
    element = safe_find_element(By.XPATH, xpath)
    if element:
        element.click()
        ActionChains(driver).key_down(copy_key).send_keys('v').key_up(copy_key).perform()
        time.sleep(random.uniform(1, 3))
        return True
    return False

def naver_log_in(id, pw):
    try:
        driver.get(naver_login_url)
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        
        # 새로운 보안 로그인 방식 체크
        try:
            # ID 입력
            id_input = safe_find_element(By.NAME, 'id')
            if id_input:
                driver.execute_script(f"document.getElementsByName('id')[0].value = '{id}'")
            else:
                copy_input("//input[@name='id']", id)
                
            time.sleep(random.uniform(1, 2))
            
            # PW 입력
            pw_input = safe_find_element(By.NAME, 'pw')
            if pw_input:
                driver.execute_script(f"document.getElementsByName('pw')[0].value = '{pw}'")
            else:
                copy_input("//input[@name='pw']", pw)
                
            time.sleep(random.uniform(1, 2))
            
            # 로그인 버튼 클릭
            login_button = safe_find_element(By.CSS_SELECTOR, '.btn_global')
            if not login_button:
                login_button = safe_find_element(By.XPATH, "//button[contains(@class, 'btn_login')]")
            
            if not safe_click(login_button):
                log_message("Login button not found", error=True)
                return False
                
            time.sleep(3)
        
            # 로그인 성공 확인
            naver_home = driver.current_url
            if naver_url in naver_home:
                log_message('Login complete')
                return True
            else:
                log_message('Login failed - Wrong URL', error=True)
                return False
                
        except Exception as e:
            log_message(f"Login error: {str(e)}", error=True)
            return False
            
    except WebDriverException as e:
        log_message(f"WebDriver error: {str(e)}", error=True)
        return False

def load_comment_history():
    try:
        if not os.path.exists(log_path):
            with open(log_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'article_id', 'user_id', 'status'])
            return []
            
        with open(log_path, 'r', encoding='utf-8') as f:
            rdr = csv.reader(f)
            next(rdr, None)
            line = []
            for imsi in rdr:
                if len(imsi) > 1:
                    line.append(imsi[1])
            log_message('Comment history loaded successfully')
            return line
    except Exception as e:
        log_message(f"Error loading comment history: {str(e)}", error=True)
        return []

def post_comment(article_id, comment_text):
    try:
        comment_input = safe_find_element(By.XPATH, '//*[@id="content"]')
        if not comment_input:
            log_message("Comment input field not found", error=True)
            return False
            
        comment_input.send_keys(comment_text)
        time.sleep(random.uniform(2, 3))
        
        submit_button = safe_find_element(By.XPATH, '//*[@id="commentSaveForm"]/fieldset/div/div/div[5]/button[2]')
        if not safe_click(submit_button):
            log_message("Comment submit button not found", error=True)
            return False
            
        with open(log_path, 'a', encoding='utf-8', newline='') as fs:
            wr = csv.writer(fs)
            wr.writerow([now_time, article_id, userid, 'complete'])
            
        log_message(f"Comment posted successfully: {article_id}")
        return True
        
    except Exception as e:
        log_message(f"Error posting comment: {str(e)}", error=True)
        return False

# 메인 실행부
def main():
    try:
        if not naver_log_in(userid, userpw):
            log_message("Login failed, exiting", error=True)
            driver.quit()
            return

        comment_history = load_comment_history()
        
        for page in range(1, 5):
            for post in range(1, 6):
                try:
                    driver.get(target_url)
                    driver.implicitly_wait(10)
                    time.sleep(random.uniform(2, 4))
                    
                    for i in range(page-1):
                        more_button = safe_find_element(By.XPATH, '//*[@id="memoList"]/div/a')
                        if not safe_click(more_button):
                            log_message("More button not found or not clickable", error=True)
                            break
                    
                    comment_button_xpath = f'//*[@id="memoList"]/ul[{page}]/li[{post}]/div/div/div[4]/a'
                    comment_button = safe_find_element(By.XPATH, comment_button_xpath)
                    if not safe_click(comment_button):
                        log_message(f"Comment button not found for page {page}, post {post}", error=True)
                        continue
                    
                    result = driver.current_url
                    try:
                        comment_board_numbers = result.split('articleid=')[1]
                    except IndexError:
                        log_message("Could not extract article ID from URL", error=True)
                        continue
                    
                    if comment_board_numbers in comment_history:
                        log_message(f"Already commented: {comment_board_numbers}")
                        continue
                    
                    comment_text = content_comment()
                    if post_comment(comment_board_numbers, comment_text):
                        comment_history.append(comment_board_numbers)
                    
                    time.sleep(random.uniform(5, 10))
                    
                except Exception as e:
                    log_message(f"Error processing page {page}, post {post}: {str(e)}", error=True)
                    continue
        
        log_message('All tasks completed successfully')
        
    except Exception as e:
        log_message(f"Unexpected error in main execution: {str(e)}", error=True)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()



