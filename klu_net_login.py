from selenium import webdriver                      # python -m pip install selenium
from selenium.webdriver.common.keys import Keys     # copy msedgedriver.exe to PATH (C:\Users\welcome\AppData\Local\Programs\Python\Python311)
from selenium.webdriver.common.by import By
from ping3 import ping, verbose_ping                # pip install ping3
import time
import requests                                     # pip install requests
import os
from dotenv import load_dotenv
load_dotenv()
klu_net_url = os.getenv("klu_net_url")
klu_net_loginid = os.getenv("klu_net_userid")
klu_net_password = os.getenv("klu_net_password")
while True:
    print("-----------------------")
    # print("Waiting for 10 Sec")
    # # time.sleep(10)
    try:
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        print("Checking for Internet at ", curr_time)
        r = requests.head("http://www.google.com/", timeout=1)
        p = int(r.status_code)
    except:
        p = 0
        print("Network Problem")
    if p == 200:
        # print("Entered into if")
        print("Network OK")
        print("waiting for 10 Sec")
        # print("-----------------------")
        time.sleep(10)
    elif p == 403:
        # print("Entered into elif")
        # p = klu_net_login()
        try:
            print("Trying to Login")
            driver = webdriver.Edge()
            driver.get(klu_net_url)
            elem = driver.find_element(By.NAME, "username")
            elem.clear()
            elem.send_keys(klu_net_loginid)
            elem = driver.find_element(By.NAME, "password")
            elem.clear()
            elem.send_keys(klu_net_password)
            # elem.send_keys(Keys.RETURN)
            elem = driver.find_element(By.XPATH,"//div[@id='loginbutton']")
            elem.click()
            time.sleep(3)
            # driver.switch_to.window(driver.window_handles[0])
            # driver.close()
            driver.minimize_window()
            print("NEtwork Logged in")
            # print("-----------------------")

        except:
            # print("Entered into except")
            print("Cannot Login")
            print("Waiting for 10 Sec")
            # print("-----------------------")
            time.sleep(10)
    else:
        print("Error Login")
        print("Waiting for 10 Sec")
        time.sleep(10)
        # print("-----------------------")