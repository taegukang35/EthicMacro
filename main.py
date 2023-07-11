from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 로그인: 포탈 간편 인증을 진행하기에 핸드폰 확인해주세요.
id = "본인포탈아이디여기에적어주세요"
driver = webdriver.Chrome()
driver.get("https://humanrights.kaist.ac.kr/pages/sub/sub0701")
driver.find_element(By.XPATH, '//*[@id="content"]/p[2]/a/img').click()
driver.find_element(By.ID, "IdInput").send_keys(id)
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/fieldset/ul/li[2]/input[1]').click()
driver.implicitly_wait(30)

# 강의 사이트 접속
driver.find_element(By.XPATH, '//*[@id="contents"]/div/div/div[2]/div[1]/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="content"]/table/tbody/tr[2]/td[3]/a[1]').click()
#driver.implicitly_wait(5)

# 강의 듣기
start = 1 #시작하는 강의 순서를 적어주세요. 처음부터 들으려면 1

for i in range(start + 1, 24):
    driver.find_element(By.XPATH, f'//*[@id="content"]/table/tbody/tr[{i}]/td[4]/a').click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'play-pause-button').send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 840)
    wait.until(EC.alert_is_present())
    da = Alert(driver)
    da.accept()
    print(f'진행 상황: {i - 1}/ 22')

print('이제 형성평가를 응시하세요!')
