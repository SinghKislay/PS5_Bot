from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
USERNAME = "XXXXXXXXXX"
PASSWORD = "XXXXXXXXXX"
CVV = "XXX"
LINK = "https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa?pid=GMCFYTWS68SAKTVV&lid=LSTGMCFYTWS68SAKTVVHXNXQO&marketplace=FLIPKART&fm=gamificationAndPersonalisation%2FrecentlyViewed&iid=GAP_RECENTLY_VIEWED_DESKTOP_HORIZONTAL_7af06263-cbf9-4b07-a0b1-56e4596b66cb.GMCFYTWS68SAKTVV&ppt=pp&ppn=pp&ssid=eu6o5u7i2o0000001621228279519&otracker=pp_recently_viewed_Recently%2BViewed_1_37.productCard.RECENTLY_VIEWED_SONY%2BPlayStation%2B5%2B%2528CFI-1008A01R%2529%2B825%2BGB%2Bwith%2BAstro%2527s%2BPlayroom_GMCFYTWS68SAKTVV_gamificationAndPersonalisation%2FrecentlyViewed_0&otracker1=pp_recently_viewed_PINNED_gamificationAndPersonalisation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_1_NA_view-all&cid=GMCFYTWS68SAKTVV"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com/account/login?ret=/")
element = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/div[1]/div[3]//form[1]//button[1]")))
username = driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]//input[1]").send_keys(USERNAME)
password = driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]/div[2]//input[1]").send_keys(PASSWORD)
login = driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]//button[1]").click()
time.sleep(1)
driver.get(LINK)

while(True):
    try:
        driver.refresh()
        element = WebDriverWait(driver, 1, 0.1).until(EC.presence_of_element_located((By.XPATH, "//div[@id='container']/div[1]/div[3]//form[1]/button[1]")))
        break
    except:
        print("Not found Yet!")
buy = driver.find_element_by_xpath("//div[@id='container']/div[1]/div[3]//form[1]/button[1]").click()
element = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="CONTINUE"]')))
found = False
try:
    cont = driver.find_element_by_xpath('//button[normalize-space()="CONTINUE"]').click()
except:
    cont = driver.find_element_by_xpath('//button[normalize-space()="Continue"]').click()


element = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//input[@maxlength="3"]')))
cvv = driver.find_element_by_xpath('//input[@maxlength="3"]').send_keys(CVV)

try:
    element = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="CONTINUE"]'))).click()
except:
    element = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Continue"]'))).click()


