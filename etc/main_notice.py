from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, os, urllib3, json, requests, ast
from selenium.webdriver.chrome.options import Options
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
options.add_argument("lang=ko_KR") # 한국어!
driver = webdriver.Chrome('innaver/chromedriver', chrome_options=options)

naver_login_url = "https://nid.naver.com/nidlogin.login" # naver login 
naver_url = 'https://www.naver.com/'
nuc_url ='https://cafe.naver.com/northpeakuser'
kan_url ='https://cafe.naver.com/campingkan' 

userid = 'tlgudlove111'
userpw = '92ghlrhks'
club_ID = '29118241'

def content_comment() :
    comment_list = ['안녕하세요. 반가워요 소중한 추억 간직하시길 기원하겠습니다.',
                    '반갑습니다. 캠핑칸과 함께 소중한 추억 간직하시길~',
                    '안녕하세요^^', 
                    '반갑습니다~!',
                    '환영합니다 즐거운시간되세요',
                    '어서오세요^^'
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


driver.get(naver_login_url)
driver.implicitly_wait(10)

copy_input('//*[@id="id"]', userid)
time.sleep(random.uniform(0,2))
copy_input('//*[@id="pw"]', userpw)
time.sleep(random.uniform(0,2))
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(random.uniform(1,3))

naver_home = driver.current_url # 현재 주소 가져오기
driver.implicitly_wait(10)

print(naver_home)

if naver_home == naver_url : 
    print("login complete") # 로그인 완료
    time.sleep(random.uniform(0,3))
    kan_welcome_url = 'https://m.cafe.naver.com/MemoList.nhn?search.clubid=' + club_ID + '&search.menuid=278'
    driver.get(kan_welcome_url)
    driver.implicitly_wait(10)
    print('Kan welcome')

    time.sleep(random.uniform(1,3))

    driver.find_element_by_xpath('//*[@id="memoList"]/ul[1]/li[1]/div/div/div[4]/a').click() # 최근댓글 번호 확인
    driver.implicitly_wait(10)

    result = driver.current_url # 현재 주소 가져오기
    comment_board_numbers = result.split('articleid=')[1]
    print('Comment_board_numbers : ', comment_board_numbers)
    comment = int(comment_board_numbers)
    len_co = len(comment_board_numbers) #글번호 자리수 

    with open('innaver/list.txt', 'r') as fs :
        line = fs.readlines() 
        line = list(map(lambda s: s.strip(), line))
        end_line = line[-1]
        end_line = end_line[:len_co]
        end_line = int(end_line)

    with open('innaver/list.txt','a') as fs : 
        for i in range(end_line + 1, comment + 1) : 
            comment_url = 'https://m.cafe.naver.com/MemoCommentView.nhn?search.clubid=' + club_ID +'&search.menuid=278&search.articleid=' + str(i)    
            driver.get(comment_url)
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1,3))
            try :
                copy_input('//*[@id="content"]', content_comment()) #내용입력
                driver.find_element_by_xpath('//*[@id="commentSaveForm"]/fieldset/div/div/div[5]/button[2]').click()
                time.sleep(random.uniform(1,3))
                fs.write(str(i) + '\n')
                print(str(i), 'complete')
            except :
                print(str(i), 'failed')
            
            time.sleep(random.uniform(2,3))
else :
    print('login fail')

# time.sleep(random.uniform(1,3))
# driver.quit()



