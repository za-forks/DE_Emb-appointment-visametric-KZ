#!/bin/python
import time
from beepy import beep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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
    current_best_date = '2022-09-16'
    i = 1
    
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
        while no_earlier_dates:
            try:
                driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object],[object Object]']//option[@value='2']").click()
                time.sleep(1)
                driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object]']//option[@value='individual']").click()
                time.sleep(1)
                earliest_date = driver.find_element(By.XPATH, "//li[@class='list-group-item']").text
            except NoSuchElementException as exc:
                print(exc)
                earliest_date = current_best_date
                
            if check_earliest_date(earliest_date):
                print("NEW APPOINTMENT DATE FOUND: ", earliest_date, ". Previous best date: ", current_best_date)
                no_earlier_dates = False
            elif earliest_date < current_best_date:
                print("earlier date found: ", earliest_date, ". Previous best date: ", current_best_date)
                current_best_date = earliest_date
                driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object],[object Object]']//option[@value='10']").click()
                print(i, end=" ")
                time.sleep(5)
            else:
                driver.find_element(By.XPATH, "//select[@values='[object Object],[object Object],[object Object],[object Object]']//option[@value='10']").click()
                print(i, end=" ")
                time.sleep(5)
            i += 1
    
    return check_earliest_date(earliest_date)


if __name__ == "__main__":
    reserve_appointment()
    for i in range(1000):
        beep(sound = "siren")
        time.sleep(0.1)
        