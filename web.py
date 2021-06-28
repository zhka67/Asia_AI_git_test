import re
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable_gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
driver.implicitly_wait(10)
category = ['Politics','Economic','Social','Culture','World','IT']
page_num = [334, 423, 400, 87, 128, 74]
df_title = pd.DataFrame()

#for l in range(0,6):
df_section_title = pd.DataFrame()
title_list = []
for k in range(45,88):
    url = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=103#&date=%2000:00:00&page={}'.format(k)
    for j in range(1,5):
        for i in range(1,6):
            try:
                driver.get(url)
                time.sleep(5)
                title = driver.find_element_by_xpath(
                '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(j,i)
                ).text
                title = (re.compile('[^가-힣 | a-z | A-Z]').sub('', title))
                print(title)
                title_list.append(title)
            except NoSuchElementException:
                print('NoSuchElementException')
df_section_title = pd.DataFrame(title_list)
df_section_title['category'] = category[3]
df_title = pd.concat([df_title,df_section_title], axis=0, ignore_index=True)
driver.close()
df_title.head(30)
df_title.to_csv('./crawling_data/naver_news_titles_20210616_cluture_45_88.csv',encoding='utf-8-sig')
print(title_list)
#//*[@id="section_body"]/ul[3]/li[1]/dl/dt[2]/a
#//*[@id="section_body"]/ul[3]/li[2]/dl/dt[2]/a