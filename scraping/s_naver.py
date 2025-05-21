#셀레니움
# import requests 필요없음
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#url 파이썬이 가지고 있는 데이터타입으로 
keyword = input("검색을 원하는 키워드로 입력해주세요 : ")
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

option_ = Options() #인스터스화 : 클래스를 그대로 가져다 쓰면 안됨. 나만의 변수로 해줘야함. 클래스는 대문자로 시작
option_.add_experimental_option("detach", True) # 자동으로 브라우저가 종료되지 않게 설정하는 옵션

driver = webdriver.Chrome(options=option_)
driver.get(base_url)
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") #.view_wrap 결과는 리스트와 동일한 데이터 타입으로 가져온다. 
print(len(results))
for i in results:
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")["href"]
    writer = i.select_one(".name").text
    dsc = i.select_one(".dsc_link").text
    print(f"제목 : {title}")
    print(f"링크 : {link}")
    print(f"작성자 : {writer}")
    print(f"글요약 : {dsc}")
    print("---------------")

driver.quit()