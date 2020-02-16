import os
from selenium import webdriver
import logging
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def dp_click_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/header/div/div[1]/button/span")
    python_button.click()
    return


def dp_click():
    time.sleep(15)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[1]/div/img")
    python_button.click()
    return

def view_dp():
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[1]/div")
    python_button.click()
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[3]/div/div/div[1]/div[2]")
    python_button.click()
    return

def remove_dp():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img")
    python_button.click()
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[4]/div")
    python_button.click()
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return

def upload_dp():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[1]/div/img")
    python_button.click()
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img")
    python_button.click()
    time.sleep(3)
    driver.find_element_by_id("app").send_keys("C://Users/lenovo/Desktop/image.png")
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div/span")
    python_button.click()
    time.sleep(3)


def change_name():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[2]/div[2]/div[1]/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(20):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("give name")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    return


def change_about():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(40):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("give about")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    return

def view_archived():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/header/div/div[1]/button/span")
    python_button.click()
    return

def view_starred():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div")
    python_button.click()
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/header/div/div[1]/button/span")
    python_button.click()
    return

def setting():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    return

def setting_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span")
    python_button.click()
    return

def notification():
    setting()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[2]")
    python_button.click()
    return

def notificaton_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span")
    python_button.click()
    setting_back()
    return

def notification_sound():
    notification()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div/div[1]/div[1]/div")
    python_button.click()
    notificaton_back()
    return

def notification_Desktop_alerts():
    notification()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div/div[2]/div[2]")
    python_button.click()
    notificaton_back()
    return

def notification_show_previews():
    notification()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div/div[3]/div[2]")
    python_button.click()
    notificaton_back()
    return

def group_chat_dots():
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/div/span")
    python_button.click()
    return

def group_info():
    group_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[1]/div")
    python_button.click()
    return

def group_info_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]/button/span")
    python_button.click()
    return

def change_group_name():
    group_info()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[2]/div[1]/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(40):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("give about")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    group_info_back()
    return

def change_group_desc():
    group_info()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/div/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(40):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("give about")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    group_info_back()
    return

def mute_group():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[3]/label/input")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div[2]")
    python_button.click()
    return

def unmute_group():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    return


def clear_group_chat():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[4]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return


def exit_group_chat():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]]")
    python_button.click()
    return


def individual_chat_dots():
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/div/span")
    python_button.click()
    return


def individual_info():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[1]/div")
    python_button.click()


def individual_chat_mute():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[3]/label/input")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div[2]")
    python_button.click()
    return


def individual_clear_chat():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[4]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return


def individual_delete_chat():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return


