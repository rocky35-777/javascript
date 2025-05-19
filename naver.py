import requests
from bs4 import BeautifulSoup

#url 파이썬이 가지고 있는 데이터타입으로 
keyword = input("검색을 원하는 키워드로 입력해주세요 : ")
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

req = requests.get(base_url)
html = req.text

soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") #.view_wrap 결과는 리스트와 동일한 데이터 타입으로 가져온다. 

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
