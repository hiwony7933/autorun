from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, os, urllib3, json, requests, ast, datetime
from selenium.webdriver.chrome.options import Options
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
options.add_argument("lang=ko_KR") # 한국어!
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

#info
naver_login_url = "https://nid.naver.com/nidlogin.login"
naver_url = 'https://www.naver.com/'
kan_url ='https://cafe.naver.com/campingkan' 

userid = 'tlgudlove'
userpw = 'tlgud063'
club_ID = '29118241'

def content_comment() :
    comment_list = ['안녕하세요. 반가워요 소중한 추억 간직하시길 기원하겠습니다.',
                    '반갑습니다. 캠핑칸과 함께 소중한 추억 간직하시길~',
                    '안녕하세요^^', 
                    '반갑습니다~!',
                    '환영합니다 즐거운시간되세요',
                    '어서오세요^^',
                    '명품 칸과 함께해요~',
                    '반갑습니다.',
                    '환영합니다.'
                    ]
    random_num = random.randint(0,len(comment_list)-1)
    return comment_list[random_num]

#클립보드에 input을 복사한 뒤 해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # 윈도우 우분투
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() #mac
    time.sleep(random.uniform(0,3))

# 리스트 인덱스 찾기
def find_index(data, target):
    res = []
    lis = data
    while True:
        try:
            res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0)) #+1의 이유 : 0부터 시작이니까
            lis = data[res[-1]+1:]
        except:
            break     
    return res

def log_in(id, pw) :
    driver.get(naver_login_url)
    driver.implicitly_wait(10)
    copy_input('//*[@id="id"]', id)
    time.sleep(random.uniform(1,2))
    copy_input('//*[@id="pw"]', pw)
    time.sleep(random.uniform(1,2))
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(3)

    naver_home = driver.current_url # 현재 주소 가져오기
    driver.implicitly_wait(10)
    return naver_home

if log_in(userid, userpw) == naver_url :
    print('login_complete')

kan_welcome_url = 'https://m.cafe.naver.com/MemoList.nhn?search.clubid=' + club_ID + '&search.menuid=278'
driver.get(kan_welcome_url)
driver.implicitly_wait(10)
time.sleep(random.uniform(1,3))


now = datetime.datetime.now()

try : 
    if naver_home == naver_url : 
        print("login complete") # 로그인 완료
        for i in range(1, 6) :
            time.sleep(random.uniform(1,3))
            kan_welcome_url = 'https://m.cafe.naver.com/MemoList.nhn?search.clubid=' + club_ID + '&search.menuid=278'
            driver.get(kan_welcome_url)
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1,3))

            xpath_insert = '//*[@id="memoList"]/ul[1]/li[' + str(i) + ']/div/div/div[4]/a'
            # 최근 댓글 클릭
            driver.find_element_by_xpath(xpath_insert).click()
            driver.implicitly_wait(10)
            result = driver.current_url # 현재 댓글 주소 가져오기
            comment_board_numbers = result.split('articleid=')[1] # 댓글 번호 분리
            comment = int(comment_board_numbers) # 정수 변환
            len_co = len(comment_board_numbers) # 댓글 번호 자리수 확인
            
            # 댓글 작성 번호 list 
            with open('./kan_list.csv', 'r') as fs :
                line = fs.readlines() # 기존 댓글 작성 번호 list
                line = list(map(lambda s: s.strip(), line)) # 개행문자\n 삭제

            find_index_ = find_index(line, comment_board_numbers)
            time.sleep(random.uniform(1,3))
            if not find_index_ :
                with open('./kan_list.csv','a') as fs : 
                    copy_input('//*[@id="content"]', content_comment()) #내용입력
                    driver.find_element_by_xpath('//*[@id="commentSaveForm"]/fieldset/div/div/div[5]/button[2]').click()
                    time.sleep(random.uniform(1,3))
                    fs.write(comment_board_numbers + '\n')
                    print(comment_board_numbers, 'content enter complete')
            else :
                print(comment_board_numbers, 'already complete')
                time.sleep(random.uniform(1,3))
                driver.quit()

        # 2페이지
        for j in range(2, 5) :
            for i in range(1, 6) :
                time.sleep(random.uniform(1,3))
                kan_welcome_url = 'https://m.cafe.naver.com/MemoList.nhn?search.clubid=' + club_ID + '&search.menuid=278'
                driver.get(kan_welcome_url)
                driver.implicitly_wait(10)
                time.sleep(random.uniform(1,3))

                click_num = 0
                while click_num < j-1 :
                    click_num = click_num + 1
                    driver.find_element_by_xpath('//*[@id="memoList"]/div/a').click()
                    time.sleep(random.uniform(1,2))
            
                xpath_insert = '//*[@id="memoList"]/ul['+ str(j) +']/li[' + str(i) + ']/div/div/div[4]/a'
                # 최근 댓글 클릭
                driver.find_element_by_xpath(xpath_insert).click()
                driver.implicitly_wait(10)
                result = driver.current_url # 현재 댓글 주소 가져오기
                comment_board_numbers = result.split('articleid=')[1] # 댓글 번호 분리
                comment = int(comment_board_numbers) # 정수 변환
                len_co = len(comment_board_numbers) # 댓글 번호 자리수 확인
                
                # 댓글 작성 번호 list 
                with open('./kan_list.csv', 'r') as fs :
                    line = fs.readlines() # 기존 댓글 작성 번호 list
                    line = list(map(lambda s: s.strip(), line)) # 개행문자\n 삭제

                find_index_ = find_index(line, comment_board_numbers)
                time.sleep(random.uniform(1,3))
                if not find_index_ :
                    with open('./kan_list.csv','a') as fs : 
                        copy_input('//*[@id="content"]', content_comment()) #내용입력
                        driver.find_element_by_xpath('//*[@id="commentSaveForm"]/fieldset/div/div/div[5]/button[2]').click()
                        time.sleep(random.uniform(1,3))
                        fs.write(comment_board_numbers + '\n')
                        print(comment_board_numbers, 'content enter complete')
                else :
                    print(comment_board_numbers, 'already complete')
                    time.sleep(random.uniform(1,3))
                    driver.quit()

    else :
        print('login fail')
        driver.quit()
except :
    print('EXIT')


