from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection:

    def test1(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "//div[@id='multi-product-search-form-1']//div[1]/ul/li[2]/a").click()
        time.sleep(2)

        departingField = driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ROUND_TRIP']/div/div[2]")
        departingField.click()
        time.sleep(2)

        # selectdate1 = driver.find_element(By.XPATH, "//div[@class='uitk-month uitk-month-double uitk-month-double-left']//div[contains(text(), 24)]")
        # selectdate1.click()
        # time.sleep(2)

        calmonth = driver.find_element(By.XPATH, "//div[@class='uitk-month uitk-month-double uitk-month-double-left']")
        validdates = calmonth.find_elements(By.TAG_NAME, "div")

        for date in validdates:
            if date.text == "30":
                date.click()
                time.sleep(2)
                break  # This is an alternative way of doing the same thing above which is finding and clicking the dates

        calmonth2 = driver.find_element(By.XPATH, "//div[@class='uitk-month uitk-month-double uitk-month-double-right']")
        validdates2 = calmonth2.find_elements(By.TAG_NAME, "div")

        for date in validdates2:
            if date.text == "20":
                date.click()
                time.sleep(2)
                break


cc = CalendarSelection()
cc.test1()
