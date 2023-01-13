import time
import json
import asyncio
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

import lib

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# url = "file:///C:/Users/thayt/Desktop/kqht01.html"
url = "https://lms.rdi.edu.vn/"

driver.get(url)

username = "194122671"
password = "@Mydung0209"

# username = "194122679"
# password = "194122679#@"

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@class="signup-form"]/div[3]/button').click()



def Click(ma_mon, so_lan, lan_lam_thu):
    lan_lam_thu += 1
    database = lib.getDataMon(ma_mon)
    data_mon = database[ma_mon]        

    time.sleep(random.randint(5,30))

    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/section/div[1]/div/div/div[3]/div/form/button').click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/section/div[1]/div/div/div[2]/div/form/button').click()
    

    
    time.sleep(random.randint(5,30))
    
    whandle = driver.window_handles[1]
    driver.switch_to.window(whandle)

    so_cauhoi = driver.find_elements(By.XPATH, '//*[@class="qtext"]')

    for r in range (1,len(so_cauhoi)+1):
        
        cauhoi = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[1]').text

        randomDapan = random.randint(1,4)

        driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div/div[2]/div[2]/div['+str(randomDapan)+']/input').click()

        dapandung_arr = lib.getDapanDung(data_mon, cauhoi )

        so_dapan = driver.find_elements(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div')
   

        for e in range (1,len(so_dapan)+1) :
            dapan = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div['+str(e)+']/div/div').text
            
            if(dapan in dapandung_arr):
                print(cauhoi)
                driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div/div[2]/div[2]/div['+str(e)+']/input').click()

        

        time.sleep(random.randint(5,30))

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/div/form/div/div[6]/input').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/div/div[3]/div/div/form/button').click()

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//*[@value='Nộp bài và kết thúc']")))

    el_ketthuc = driver.find_elements(By.XPATH, "//*[@value='Nộp bài và kết thúc']")



    for r in range (0,len(el_ketthuc)):
        el_ketthuc[r].click()




    for r in range (1,len(so_cauhoi)+1):
        
        cauhoi = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[1]').text
        dapandung_el = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[2]/div/div')

        dapandung = dapandung_el.text.split("The correct answer is: ")[1]


        countCheckCauhoi = (lib.checkDataMon(data_mon, cauhoi, dapandung ))

        if(countCheckCauhoi==0):

            so_dapan = driver.find_elements(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div')

            dapan = []

            for e in range (1,len(so_dapan)+1) :

                dapan_el = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div['+str(e)+']/div/div')
                dapan.append(dapan_el.text)

            data = {
                "cauhoi": cauhoi,
                "dapan": dapan,
                "dapandung": dapandung
            }
        
            data_mon.append(data)
        else:
            print("Da ton tai: " + cauhoi)


    with open('data.json', 'w',encoding='utf8') as outfile:
        json.dump(database, outfile, ensure_ascii=False)

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/div/div/input').click()


    whandle = driver.window_handles[0]
    driver.switch_to.window(whandle)

    # print(str(so_lan) +' - ' + str(lan_lam_thu))

    if(int(so_lan)< int(lan_lam_thu)):
        input('Da lam ' + str(lan_lam_thu))
       
        print(' ')
        so_lan = input('Ban muon lam bao nhieu lan?   ')
        print(' ')

        if(so_lan==''):
            so_lan =0
        ma_mon = driver.find_element(By.XPATH, '//header/div/div/div/div[2]/div[1]/nav/ol/li[3]/a').text

        lan_lam_thu = 1

        Click(ma_mon, so_lan, lan_lam_thu)

    Click(ma_mon, so_lan, lan_lam_thu)

    
    
print(' ')
so_lan = input('Ban muon lam bao nhieu lan?    ')   

print(' ')
if(so_lan==''):
    so_lan =0
ma_mon = driver.find_element(By.XPATH, '//header/div/div/div/div[2]/div[1]/nav/ol/li[3]/a').text

lan_lam_thu = 1

Click(ma_mon, so_lan, lan_lam_thu)

# git add . && git commit -m "commit" && git push -u origin main