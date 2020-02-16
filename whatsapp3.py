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
    time.sleep(4)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div")
    python_button.click()
    actions = ActionChains(driver)
    no = int(input("enter number"))
    for x in range(no):
        num =int(input("enter a number to add"))
        actions.send_keys(num)
        actions.send_keys(Keys.ENTER).perform()
        num=0

    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span")
    python_button.click()
    return


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


def search_selection():
    python_button = driver.find_elements_by_xpath("//*[@id='side']/div[1]/div/label/input")
    python_button.click()


def dropdown():
    *****
    img = driver.find_element_by_xpath('//img')
    actionChains = ActionChains(driver)
    actionChains.move_to_element(img).context_click()
    return


def archive():

    dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[1]/div")
    python_button.click()
    return


def mute_notifs():
    dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[2]/div")
    python_button.click()
    return


def exit_group():
    dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[3]/div")
    python_button.click()
    return

def pin_chat():
    dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[4]/div")
    python_button.click()
    return


def mark_unread():
    dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[5]/div")
    python_button.click()
    return

def delete_chat():
    dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[3]/div")
    python_button.click()
    return

def viewing_status():
    python_button = driver.find_elements_by_xpath("//*[@id='side']/header/div[2]/div/span/div[1]/div/span")
    python_button.click()
    *****
    return







if __name__ == '__main__':
    chromedriver = "C:\webdrivers\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://web.whatsapp.com")
