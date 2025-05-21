from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#클래스, 아이디 css_selector를 이용해서 원하는 값을 가져오기 위한 패키지
from selenium.webdriver.common.by import By
#키보드의 입력 형태를 코드로 작성하기 위해 사용하는 패키지
from selenium.webdriver.common.keys import Keys

#url 파이썬이 가지고 있는 데이터타입으로 
base_url = "https://kream.co.kr/"

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}


option_ = Options() #인스터스화 : 클래스를 그대로 가져다 쓰면 안됨. 나만의 변수로 해줘야함. 클래스는 대문자로 시작
option_.add_experimental_option("detach", True) # 자동으로 브라우저가 종료되지 않게 설정하는 옵션
option_.add_argument(f"User-Agent={header_user}")


driver = webdriver.Chrome(options=option_)
driver.get(base_url)
time.sleep(1)

#돋보기 누르기
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
 #클래스명 3개

#검색어 입력
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
#엔터 코드
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(2)

for i in range(20):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

for item in items : 
    product_name = item.select_one(".translated_name").text
    if "후드" in product_name :    
        category = "상의"
        product_brand = item.select_one(".brand-name").text
        product_price = item.select_one(".amount").text

        print(f"카테고리 : {category}")
        print(f"브랜드 : {product_brand}")
        print(f"제품명 : {product_name}")
        print(f"가격 : {product_price}")
        print("--------------")

# driver.quit()
