# -*- coding: utf-8 -*-
# 2018.10.31 네이버 IT랭킹 10/30일자 20개 수집 

from selenium import webdriver
from bs4 import BeautifulSoup

def naver_ITnews() :
    FILE_NAME = "news.txt"
    f = open(FILE_NAME, "a", encoding="utf8")

    driver = webdriver.Chrome('C:/Users/KyeongMin/Desktop/App/chrome/chromedriver.exe')

    driver.implicitly_wait(3)

    news_url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date=20181030'
    driver.get(news_url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    for line in soup.select('div.ranking') :
        for number in range(0,30):
            article_url = line.select('div.ranking_headline > a')[number].get('href')
            article_url = 'https://news.naver.com' + article_url

            # 기사 내용
            driver.get(article_url)
            html_detail = driver.page_source
            soup_detail = BeautifulSoup(html_detail, 'html.parser')

            for article in soup_detail.select('div#articleBodyContents'):
                title = soup_detail.select("h3#articleTitle")[0].text.strip()
                title = title + "\n"
                article.script.decompose()
                article = article.text.strip() + "\n"

                print("#####################################################")
                print(title)
                print(article)
                f.write(title)
                f.write(article)
                f.write("\n\n")

    f.close()
    driver.quit()
    
if __name__ == "__main__":
    naver_ITnews()