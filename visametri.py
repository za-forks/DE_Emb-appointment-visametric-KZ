#!/bin/python
import time
from beepy import beep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def check_earliest_date(earliest_date):
    if earliest_date < '2022-08-25':
        return True
    else:
        return False


def reserve_appointment():
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    # service = Service(executable_path=ChromeDriverManager().install())
    service = Service(executable_path=PATH)
    driver = webdriver.Chrome(service=service)
    no_earlier_dates = True
    
    while no_earlier_dates:
        print("=" * 50)
        LOGIN_PAGE = "https://appointment.visametric.com/"
        driver.get(LOGIN_PAGE)
        time.sleep(5)
        print(f"Open {LOGIN_PAGE} in chrome")
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object]']//option[@value='KZ']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object]']//option[@value='DE']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary pull-right']").click()
        #driver.find_element(By.LINK_TEXT, "Continue").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object]']//option[@value='2']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object]']//option[@value='normal']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object],[object Object]']//option[@value='04']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object],[object Object]']//option[@value='2']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object]']//option[@value='individual']").click()
        time.sleep(1)
        earliest_date = driver.find_element(By.XPATH, "//li[@class='list-group-item']").text
        if check_earliest_date(earliest_date):
            print("earlier date found!")
            no_earlier_dates = False
    
    return check_earliest_date(earliest_date)


if __name__ == "__main__":
    reserve_appointment()
    for i in range(1000):
        beep(sound = "siren")
        time.sleep(0.1)
        