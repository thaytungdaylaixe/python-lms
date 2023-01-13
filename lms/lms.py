import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "file:///C:/Users/thayt/Desktop/kqht01.html"
# url = "https://lms.rdi.edu.vn/"

driver.get(url)

# username = "194122671"
# password = "@Mydung0209"

# driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
# driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
# driver.find_element(By.XPATH, '//*[@class="signup-form"]/div[3]/button').click()

input('Press Enter to continue ...')

# so_cauhoi = driver.find_elements(By.XPATH, '//form[@id="responseform"]//*[@class="qtext"]')

so_cauhoi = driver.find_elements(By.XPATH, '//form[@id="responseform"]//*[@class="qtext"]')

alldata=[]

for r in range (0,len(so_cauhoi)) :   
    so_cautraloi = so_cauhoi[r].find_elements(By.XPATH, '..//*[@class="answer"]/div/div/div')
   
    dapandung = '<Tên_người_dùng>@<Tên_miền>'

    so_cauhoi[r].find_elements(By.XPATH, '..//*[@class="answer"]/div/input')[0].click()

    for e in range (0,len(so_cautraloi)) :
      if( dapandung == so_cautraloi[e].text):
        print(so_cautraloi[e].text)
        so_cauhoi[r].find_elements(By.XPATH, '..//*[@class="answer"]/div/input')[e].click() 
    

   



input('Press Enter to continue ...')




# for r in range (0,len(so_cauhoi)) :
#     cauhoi_el = so_cauhoi[r]
#     so_cautraloi = cauhoi_el.find_elements(By.XPATH, '..//*[@class="answer"]/div/div/div')

#     dapan = []

#     for e in range (0,len(so_cautraloi)) :
#         dapan.append(so_cautraloi[e].text)

#     data = {
#         "cauhoi": cauhoi_el.text,
#         "dapan": dapan,
#         "dapandung": '04'
#     }

   

#     alldata.append(data)


# # //*[@id="question-166030-1"]/div[2]/div/div[1]

# print(alldata)

# input('Press Enter to continue ...')

# driver.close()
# git add . && git commit -m "commit" && git push -u origin main

# //*[@class="signup-form"]/div[3]/button