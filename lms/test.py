# import time
# import json
# import asyncio
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# import lib

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# url = "file:///C:/Users/thayt/Desktop/1.html"
# # url = "https://lms.rdi.edu.vn/"

# driver.get(url)


# # WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//*[@value='Nộp bài và kết thúc']")))
# el_ketthuc = driver.find_elements(By.XPATH, "//*[@value='Nộp bài và kết thúc']")



# for r in range (0,len(el_ketthuc)):
#     print(r)
#     print(el_ketthuc[r].get_attribute('class'))

so_lan = 1
so_lan +=1

print(so_lan)


