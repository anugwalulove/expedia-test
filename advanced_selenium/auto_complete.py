from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete:
    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        partialText = "Del"
        textToSelect = "Delhi (DEL - Indira Gandhi Intl.)"

        driver.find_element(By.XPATH, "//div[@id='multi-product-search-form-1']//div[1]/ul/li[2]/a").click()
        time.sleep(2)

        textElement = driver.find_element(By.XPATH, "//div[@class='uitk-input-swapper-start-input']")
        textElement.click()

        textElement2 = driver.find_element(By.XPATH, "//input[@id='origin_select']")
        textElement2.send_keys(partialText)
        time.sleep(2)

        dp = driver.find_element(By.XPATH, "//button[@class='uitk-action-list-item-link']")
        inner_html = dp.get_attribute("innerHTML")
        print(inner_html)





cc = AutoComplete()
cc.test()