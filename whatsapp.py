import time
import datetime as dt
import json
import os
import requests
import shutil
import pickle
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def send_messages():
    action = ActionChains(driver)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    button.click()
    name = input("Enter the name")
    action.send_keys(name)
    action.send_keys(Keys.ENTER).perform()
    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    button.click()
    message = input("Enter the message")
    action1 = ActionChains(driver)
    action1.send_keys(message)
    action1.send_keys(Keys.ENTER).perform()


def send_attachments():
    action = ActionChains(driver)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    button.click()
    name = input("Enter the name")
    action.send_keys(name)
    action.send_keys(Keys.ENTER).perform()
    button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]")
    button.click()
    query = input("1 - Photo \n2 - Camera \n3 - Document \n4 - Contacts")
    if query == "1":
        button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button")
        button.click()
    elif query == "2":
        button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[2]/button")
        button.click()
    elif query == "3":
        button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button")
        button.click()
    elif query == "4":
        button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[4]/button")
        button.click()


def get_last_message_for():
    name = input()
    messages = list()
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for i in soup.find_all("div", class_="FTBzM message-in"):
        message = i.find("div", class_="_12pGw")
        if message:
            messages.append(message.text)
    messages = list(filter(None, messages))
    print(messages)


def send_picture():
    name = input()
    caption = input()
    picture_location = "/home/bolt/Pictures/201320.jpg"
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)  # we will send the name to the input key box
    try:
        attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
        send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span'
        attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'
        attach_btn = driver.find_element_by_xpath(attach_xpath)
        attach_btn.click()
        time.sleep(1)
        attach_img_btn = driver.find_element_by_xpath(attach_type_xpath)
        attach_img_btn.send_keys(picture_location)  # get current script path + img_path
        time.sleep(1)
        if caption:
            caption_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]"
            send_caption = driver.find_element_by_xpath(caption_xpath)
            send_caption.send_keys(caption)
        send_btn = driver.find_element_by_xpath(send_file_xpath)
        send_btn.click()

    except (NoSuchElementException, ElementNotVisibleException) as e:
        print(str(e))


def send_document():
    name = input()
    caption = input()
    document_location = "/home/bolt/Documents/BTech First Year Curriculum Booklet.pdf"
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    try:
        attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
        send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span'
        attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input'
        attach_btn = driver.find_element_by_xpath(attach_xpath)
        attach_btn.click()
        time.sleep(1)
        attach_img_btn = driver.find_element_by_xpath(attach_type_xpath)
        attach_img_btn.send_keys(document_location)
        time.sleep(1)
        send_btn = driver.find_element_by_xpath(send_file_xpath)
        send_btn.click()

    except (NoSuchElementException, ElementNotVisibleException) as e:
        print(str(e))


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.whatsapp.com/')
    # send_messages()
    # send_attachments()
    # get_last_message_for()
    send_picture()
