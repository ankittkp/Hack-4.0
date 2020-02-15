from selenium import webdriver
import logging
import time

if __name__ == '__main__':
    LOG_FILENAME = 'logger.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info('This message should go to the log file')
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.whatsapp.com/')

    test()
