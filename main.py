from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import os

USERNAME = "XXXXXXXXXX"
PASSWORD = "XXXXXXXXXX"
CVV = "XXX"
LINK = "https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa?pid=GMCFYTWS68SAKTVV&lid=LSTGMCFYTWS68SAKTVVHXNXQO&marketplace=FLIPKART&fm=gamificationAndPersonalisation%2FrecentlyViewed&iid=GAP_RECENTLY_VIEWED_DESKTOP_HORIZONTAL_7af06263-cbf9-4b07-a0b1-56e4596b66cb.GMCFYTWS68SAKTVV&ppt=pp&ppn=pp&ssid=eu6o5u7i2o0000001621228279519&otracker=pp_recently_viewed_Recently%2BViewed_1_37.productCard.RECENTLY_VIEWED_SONY%2BPlayStation%2B5%2B%2528CFI-1008A01R%2529%2B825%2BGB%2Bwith%2BAstro%2527s%2BPlayroom_GMCFYTWS68SAKTVV_gamificationAndPersonalisation%2FrecentlyViewed_0&otracker1=pp_recently_viewed_PINNED_gamificationAndPersonalisation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_1_NA_view-all&cid=GMCFYTWS68SAKTVV"

mutex = threading.Lock()


def pre_order():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.flipkart.com/account/login?ret=/")
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/div[1]/div[3]//form[1]//button[1]")))
    driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]//input[1]").send_keys(USERNAME)
    driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]/div[2]//input[1]").send_keys(PASSWORD)
    driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]//button[1]").click()
    time.sleep(1.5)
    driver.get(LINK)

    while(True):
        try:
            WebDriverWait(driver, 4, 0.1).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/div[1]/div[3]//form[1]/button[1]")))
            
            break
        except:
            driver.refresh()
            print("Not found Yet!")
    
    mutex.acquire()
    driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]/button[1]").click()
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="CONTINUE"]')))
    try:
        driver.find_element_by_xpath('//button[normalize-space()="CONTINUE"]').click()
    except:
        driver.find_element_by_xpath('//button[normalize-space()="Continue"]').click()


    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//input[@maxlength="3"]')))
    driver.find_element_by_xpath('//input[@maxlength="3"]').send_keys(CVV)

    try:
        WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="CONTINUE"]'))).click()
    except:
        WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Continue"]'))).click()
    mutex.release()


if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))
    
    arr = [False]

    t1 = threading.Thread(target=pre_order, args=())
    time.sleep(2.5)
    t2 = threading.Thread(target=pre_order, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
  
    
    


