from selenium import webdriver                      # python -m pip install selenium
from selenium.webdriver.common.keys import Keys     # Install Firefox and GeckoDriver
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
    try:
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        print("Checking for Internet at ", curr_time)
        r = requests.head("http://www.google.com/", timeout=1)
        p = int(r.status_code)
    except:
        p = 0
        print("Network Problem")
    
    if p == 200:
        print("Network OK")
        print("waiting for 10 Sec")
        time.sleep(10)
    elif p == 403:
        try:
            print("Trying to Login")
            driver = webdriver.Firefox()  # Changed to Firefox
            driver.get(klu_net_url)
            elem = driver.find_element(By.NAME, "username")
            elem.clear()
            elem.send_keys(klu_net_loginid)
            elem = driver.find_element(By.NAME, "password")
            elem.clear()
            elem.send_keys(klu_net_password)
            elem = driver.find_element(By.XPATH, "//div[@id='loginbutton']")
            elem.click()
            time.sleep(3)
            driver.minimize_window()  # This may not work as expected on Linux
            print("Network Logged in")
        except Exception as e:
            print("Cannot Login:", e)
            print("Waiting for 10 Sec")
            time.sleep(10)
    else:
        print("Error Login")
        print("Waiting for 10 Sec")
        time.sleep(10)
        
#------     Read me     ----------------
        
#Install Required Packages:

#Ensure that you have Firefox installed on your CentOS 7 system.
#Install the GeckoDriver, which is required for Selenium to control Firefox. You can download it from GeckoDriver releases and place it in a directory that is in your PATH, or you can install it using a package manager if available.
# GeckoDriver: Make sure that GeckoDriver is installed and accessible in your system's PATH. You can verify this by running geckodriver --version in the terminal.

#----------------------------------------

#Minimize Window: The driver.minimize_window() function may not work as expected in a headless environment or a non-GUI environment. If you are running this on a server without a GUI, consider running Firefox in headless mode by using:

#from selenium.webdriver.firefox.options import Options

#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)

#------------------------------------------------

#Dependencies: Ensure all required Python packages (selenium, requests, ping3, python-dotenv) are installed in your environment.
#Environment Variables: Make sure the .env file is set up correctly with the necessary variables for the URL, username, and password.