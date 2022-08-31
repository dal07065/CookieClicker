import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")
#DELAY_MS = 3
x = 0
wait = WebDriverWait(driver, 30)
button = wait.until(element_to_be_clickable((By.ID, "langSelect-EN")))
button.click()
wait = WebDriverWait(driver, 30)
button = wait.until(element_to_be_clickable((By.ID, "bigCookie")))
count = 0

while x < 100000:

    button.click()


    #driver.find_element_by_id("bigCookie").click()
    x += 1
    #delay = DELAY_MS / 1000
    #time.sleep(delay)

    try:
        if count <= 18 and x%100 == 0:
            wait = WebDriverWait(driver, 1)
            driver.find_element(By.XPATH, "//div[@id='product"+str(count)+"'][@class='product unlocked enabled']").click()
            print("Product " + str(count) + "is clickable")
            count += 1
    except WebDriverException:
        print("Product " + str(count) + "is not clickable")
