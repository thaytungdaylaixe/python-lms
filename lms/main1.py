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

# url = "file:///C:/Users/thayt/Desktop/kqht01.html"
url = "https://lms.rdi.edu.vn/"

driver.get(url)

# username = "194122671"
username = "194122679"
password = "@Mydung0209"



driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@class="signup-form"]/div[3]/button').click()


def Click(data_mon):
    time.sleep(2)
    whandle = driver.window_handles[1]
    driver.switch_to.window(whandle)

    so_cauhoi = driver.find_elements(By.XPATH, '//*[@class="qtext"]')

    for r in range (1,len(so_cauhoi)+1):
        
        cauhoi = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[1]').text

        randomDapan = random.randint(1,4)

        driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div/div[2]/div[2]/div['+str(randomDapan)+']/input').click()

        dapandung_arr = lib.getDapanDung(data_mon, cauhoi )

        so_dapan = driver.find_elements(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div')

        cauhoi_datontai = 0

        for e in range (1,len(so_dapan)+1) :
            dapan = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div['+str(e)+']/div/div').text
            
            if(dapan in dapandung_arr):   
                cauhoi_datontai +=1             
                driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div/div[2]/div[2]/div['+str(e)+']/input').click()

        if(cauhoi_datontai == 0):
            print(style.RED + cauhoi)
        
        time.sleep(random.randint(5,10))

    time.sleep(2)   

    print('----------------------------------------------------------------')

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/div/form/div/div[6]/input').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/div/div[3]/div/div/form/button').click()

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//*[@value='Nộp bài và kết thúc']")))

    el_ketthuc = driver.find_elements(By.XPATH, "//*[@value='Nộp bài và kết thúc']")

    for r in range (0,len(el_ketthuc)):
        el_ketthuc[r].click()


def Btvn(data_mon):
    print(data_mon)

def Save(database, so_cau ):
    data_mon = database[ma_mon] 
    so_cauhoi = driver.find_elements(By.XPATH, '//*[@class="qtext"]')

    for r in range (1,len(so_cauhoi)+1):
        
        cauhoi = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[1]').text
        dapandung_el = driver.find_element(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[2]/div/div')

        dapandung = dapandung_el.text.split("The correct answer is: ")[1]


        countCheckCauhoi = (lib.checkDataMon(data_mon, cauhoi, dapandung ))

        if(countCheckCauhoi==0):

            so_dapan = driver.find_elements(By.XPATH, '//form/div/div['+str(r)+']/div[2]/div[1]/div[2]/div[2]/div')

            so_cau +=1
            print(so_cau + ' - ' + cauhoi)

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

    with open('data.json', 'w',encoding='utf8') as outfile:
        json.dump(database, outfile, ensure_ascii=False)

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/section[1]/div/div/input').click()


def Main(ma_mon, so_lan, lan_lam_thu):
    lan_lam_thu += 1
    database = lib.getDataMon(ma_mon)
    data_mon = database[ma_mon] 

    so_cau = len(data_mon)     

    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'Thực hiện lại đề thi')]") .click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//*[contains(text(), 'Tiếp tục lần kiểm tra cuối cùng')]") .click()
    
    # Bai tap ---------------------------------------------------------------
    time.sleep(3)

    if(len(driver.window_handles)==1):
        Btvn(data_mon)
    else:
        Click(data_mon)
    # end bai tap ---------------------------------------------------------------

    # Luu ----------------------------------------------------------------
    Save(database, so_cau )
    # End Luu ----------------------------------------------------------------

    whandle = driver.window_handles[0]
    driver.switch_to.window(whandle)

    print(' ')
    print(style.GREEN + 'So cau : ' + str(so_cau) + ' - Da lam ' + str(lan_lam_thu)+' lan' + style.RESET) 
    print(' ')

    if(int(so_lan)<= int(lan_lam_thu)):    
        so_lan = lib.solanLambai()
        ma_mon = driver.find_element(By.XPATH, '//header/div/div/div/div[2]/div[1]/nav/ol/li[3]/a').text
        lan_lam_thu = 0
        Main(ma_mon, so_lan, lan_lam_thu)

    Main(ma_mon, so_lan, lan_lam_thu)

    
    


so_lan = lib.solanLambai()
ma_mon = driver.find_element(By.XPATH, '//header/div/div/div/div[2]/div[1]/nav/ol/li[3]/a').text
lan_lam_thu = 0
Main(ma_mon, so_lan, lan_lam_thu)

# git add . && git commit -m "commit" && git push -u origin main