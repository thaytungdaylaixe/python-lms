import time
import json
import asyncio
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import lib

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "file:///C:/Users/thayt/Desktop/kqht01.html"
# url = "https://lms.rdi.edu.vn/"

driver.get(url)



def Click(ma_mon):
    database = lib.getDataMon(ma_mon)
    data_mon = database[ma_mon]    

    input('Press Enter to continue ...')

    so_cauhoi = driver.find_elements(By.XPATH, '//*[@class="qtext"]')

    for r in range (1,len(so_cauhoi)+1):
        
        cauhoi = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[1]').text

        randomDapan = random.randint(1,4)

        driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div/div[2]/div[2]/div['+str(randomDapan)+']/input').click()

        dapandung_arr = lib.getDapanDung(data_mon, cauhoi )

        so_dapan = driver.find_elements(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div')

        input('Press Enter to continue ...'+str(randomDapan) + str(dapandung_arr[0]))

        for e in range (1,len(so_dapan)+1) :
            dapan = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div['+str(e)+']/div/div').text
            
            if(dapan in dapandung_arr):
                driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div/div[2]/div[2]/div['+str(e)+']/input').click()
         


    

ma_mon = 'D_Intro_I_DK22TT80161'
Click(ma_mon)
input('Press Enter to continue ...')


# chooseInput = input('Press /n Chon 2: Thoat')

# print(chooseInput)