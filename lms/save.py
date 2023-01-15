import time
import json
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import lib

import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "file:///C:/Users/thayt/Desktop/s.html"
# url = "https://lms.rdi.edu.vn/"

driver.get(url)



def SaveData(ma_mon):
    database = lib.getDataMon(ma_mon)
    data_mon = database[ma_mon]    

    so_cau = len(data_mon)     


    so_cauhoi = driver.find_elements(By.XPATH, '//*[@class="qtext"]')

    for r in range (1,len(so_cauhoi)+1):
        
        cauhoi = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[1]').text
        dapandung_el = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[2]/div/div')

        dapandung = dapandung_el.text.split("The correct answer is: ")[1]


        countCheckCauhoi = (lib.checkDataMon(data_mon, cauhoi, dapandung ))

        if(countCheckCauhoi==0):

            so_cau +=1

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

            print(' ')
            print(style.GREEN + 'So cau : ' + str(so_cau) + ' - '+cauhoi + style.RESET)        
            print(' ')
        


    with open('data.json', 'w',encoding='utf8') as outfile:
        json.dump(database, outfile, ensure_ascii=False)
   



ma_mon = input(style.GREEN + 'Moi ban nhap mã mon ...' + style.RESET)
SaveData(ma_mon)


# chooseInput = input('Press /n Chon 2: Thoat')

# print(chooseInput)