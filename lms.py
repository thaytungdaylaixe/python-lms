import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://lms.rdi.edu.vn/")

username = "194122671"
password = "@Mydung0209"

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

driver.find_element(By.XPATH, '//*[@class="signup-form"]/div[3]/button').click()

time.sleep(100)

# driver.close()

# //*[@class="signup-form"]/div[3]/button