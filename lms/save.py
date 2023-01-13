import time
import json
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import lib

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "file:///C:/Users/thayt/Desktop/1.html"
# url = "https://lms.rdi.edu.vn/"

driver.get(url)



def SaveData(ma_mon):
    database = lib.getDataMon(ma_mon)
    data_mon = database[ma_mon]    

    input('Press Enter to continue ...')

    so_cauhoi = driver.find_elements(By.XPATH, '//*[@class="qtext"]')

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
   


ma_mon = 'D_Intro_I_DK22TT80161'
SaveData(ma_mon)


# chooseInput = input('Press /n Chon 2: Thoat')

# print(chooseInput)