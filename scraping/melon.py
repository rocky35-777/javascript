import requests
from bs4 import BeautifulSoup
#사이트 분석하는 것이 가장 중요하다. 어떻게 구분할 것인가?

#유저 정보 입력_사람이다!
header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
base_url = "https://www.melon.com/chart/index.htm"

req = requests.get(base_url, headers=header_user)
html = req.text

soup = BeautifulSoup(html, "html.parser")
print(soup)

# lst50100 = soup.select(".lst50", ".lst100") 이렇게하면 한번에 할 수 있다.
lst50 = soup.select(".lst50") #1~50위까지 정보
lst100 = soup.select(".lst100") #51~100위까지 정보 
lst_all = lst50 + lst100

# 순위, 제목, 가수, 앨범 제목
# 클래스명 찾는 것이 중요! 
# 가장 편한 방법으로 짜야지 스크랩핑 하는 의미가 있다. 
# 복잡하면 오래걸리고 의미가 없음 (엑셀 또는 스크린샷이 나을수도...)
# rank = i.select_one(".rank").text
# print(f"[순위] : {rank}")
for rank, i in enumerate(lst_all, 1) : 
    rank = i.select_one(".rank").text
    title = i.select_one(".ellipsis.rank01 a").text #클래스명은 붙여서, 태그명은 띄어서 or > 화살표로 표기
    singer = i.select_one(".ellipsis.rank02 > a").text
    album = i.select_one(".ellipsis.rank03 > a").text
    print(f"[순위] : {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] : {singer}")
    print(f"[앨범] : {album}")
    print("----------------------------<")
