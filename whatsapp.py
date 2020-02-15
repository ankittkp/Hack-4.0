import os
from selenium import webdriver
import logging
import time


def dp_click():
    time.sleep(20)
    print("test")
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[1]/div/img")
    python_button.click()
    return


if __name__ == '__main__':
    LOG_FILENAME = 'logger.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logging.info('This message should go to log file')
    chromedriver = "C:\webdrivers\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    driver.get("https://web.whatsapp.com")

    dp_click()



