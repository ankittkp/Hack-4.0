from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def logout():
    time.sleep(40)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div")
    python_button.click()
    return


def groupcreation():
    time.sleep(30)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div")
    python_button.click()
    no = int(input("enter number"))
    for x in range(no):
        actions = ActionChains(driver)
        num =int(input("enter a number to add"))
        actions.send_keys(num)
        actions.send_keys(Keys.ENTER).perform()

    python_button = driver.find_elements_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/span/div")
    python_button.click()
    python_button = driver.find_elements_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[2]/div")
    python_button.click()
    #uploadingphoto
    python_button = driver.find_elements_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]")
    python_button.click()
    actions = ActionChains(driver)

    name = input("enter the name of group")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()


    return




def downloading_media():
    python_button = driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[13]/div/div[1]/div/div/div[3]/div[1]/button/span[2]")
    python_button.click()

def blocking():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[4]/div[2]")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div[2]")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div")
    python_button.click()
    return




def chat_selection():
    time.sleep(20)
    python_button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    python_button.click()
    actions = ActionChains(driver)
    name = input("enter the name of chat to select")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()

    return

def group_info():
    chat_selection()
    python_button = driver.find_elements_by_xpath("//*[@id='main']/header/div[2]/div[2]/span")
    python_button.click()
    return




#def dropdown():
    #time.sleep(4)
   # chat_selection()
    #img = driver.find_element_by_class_name("_19RFN")
    #actionChains = ActionChains(driver)
    #actionChains.double_click(img).perform()
    #return


def archive():

    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[1]/div")
    python_button.click()
    return


def mute_notifs():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[2]/div")
    python_button.click()
    return


def exit_group():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[3]/div")
    python_button.click()
    return

def pin_chat():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[4]/div")
    python_button.click()
    return


def mark_unread():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[5]/div")
    python_button.click()
    return

def delete_chat():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[3]/div")
    python_button.click()
    return

def viewing_status():
    python_button = driver.find_elements_by_xpath("//*[@id='side']/header/div[2]/div/span/div[1]/div/span")
    python_button.click()
    chat_selection()
    return


