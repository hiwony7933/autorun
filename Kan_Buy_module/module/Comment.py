from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from bs4 import BeautifulSoup as bs


class Comment(object) :
    def comment_last(self) :    
        self.driver.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li[1]/div/a[1]/strong').click()
        self.driver.implicitly_wait(10)
        com_url = self.driver.current_url
        comment_board_numbers = com_url.split('articles/')[1] # 댓글 번호 분리
        comment_board_numbers = comment_board_numbers.split('?fromList')[0] # 댓글 번호 분리
        self.driver.get('https://m.cafe.naver.com/ca-fe/web/cafes/'+ self.cafeid +'/articles/' + comment_board_numbers + '/comments?fromList=true')
        self.content_comment('//*[@id="app"]/div/div/div[3]/div/div/div/div/div')
        # self.content_comment('//*[@id="cbox"]')

    def content_comment(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()
        elem.send_keys('1')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[3]/div/div[2]/button[2]').click()
        self.textBr('댓글작성완료')
