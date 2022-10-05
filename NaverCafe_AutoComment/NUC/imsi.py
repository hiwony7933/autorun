from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, random, json, datetime, csv

# site url
naver_login_url = "https://nid.naver.com/nidlogin.login"
naver_url = 'https://www.naver.com/'

# file path
log_path = './log.csv'
config_path = './config.json'
comment_path = './comment.csv'

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

# driver options
options = webdriver.ChromeOptions()
options.add_argument('headless') # 백그라운드실행
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
# options.add_argument("lang=ko_KR") # 한국어!
options.add_argument('window-size=1920x1080')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("--disable-gpu")
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

# random comment
def content_comment():
    with open('./comment.csv','r',encoding='utf-8') as f:
        imsi_comment = csv.reader(f)
        comment_list =[]
        for i in imsi_comment :
            comment_list.append(i[0])
        random_num = random.randint(0,len(comment_list)-1)
    return comment_list[random_num]

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


def naver_log_in(id, pw) :
    driver.get(naver_login_url)
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1,2))
    # java script 
    driver.execute_script("document.getElementsByName('id')[0].value = \'" + id + "\'")
    time.sleep(random.uniform(1,2))
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    time.sleep(random.uniform(1,2))
    driver.find_element_by_css_selector('.btn_global').click()
    time.sleep(3)

    naver_home = driver.current_url # 현재 주소 가져오기
    driver.implicitly_wait(10)
    
    if naver_home == naver_url :         
        print(now_time,'login_complete')
    else :
        print(now_time,'login_failed')
        driver.quit()   

# login 
try : 
    naver_log_in(userid, userpw) 
except : 
    print('Login fail : EXIT')


# 댓글 작성 번호 list 
try :
    with open(log_path, 'r', encoding='utf-8') as f :
        rdr = csv.reader(f)
        line =[]
        for imsi in rdr:
            line.append(imsi[1])
        print('list up complete')
except :
    print('Check list.csv path : ./log.csv')


try :
    for i in range(1,21) : 
        driver.get(target_url)
        driver.implicitly_wait(10)
        time.sleep(random.uniform(2,3))
        driver.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li['+str(i) +']/div/a[1]/strong').click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(2,3))
        result = driver.current_url 
        comment_board_numbers = result.split('articles/')[1] # 댓글 번호 분리
        comment_board_numbers = comment_board_numbers.split('?fromList')[0] # 댓글 번호 분리
        find_index_ = find_index(line, comment_board_numbers)
        # print(comment_board_numbers)

        driver.get('https://m.cafe.naver.com/ca-fe/web/cafes/26163062/articles/'+comment_board_numbers+'/comments?fromList=true&menuId=67')
        driver.implicitly_wait(10)
        time.sleep(random.uniform(2,3))

        if not find_index_ : 
            with open(log_path, 'a', encoding='utf-8', newline='') as fs :
                driver.find_element_by_xpath('//*[@id="cbox"]').send_keys(content_comment())
                time.sleep(random.uniform(2,3))
                driver.find_element_by_css_selector('.CommentWriteUpload__btn_register').click()

                driver.implicitly_wait(10)
                time.sleep(random.uniform(2,3))
                wr = csv.writer(fs)
                wr.writerow([now_time, comment_board_numbers, userid, 'complete' ])
                print(now_time, comment_board_numbers, 'complete')
        else :
            print(now_time, comment_board_numbers, 'already')
            time.sleep(random.uniform(2,3))
            driver.quit()
            break       

    driver.quit()
    print('Complete : EXIT')

except :
    print('Already : EXIT')
    driver.quit()


