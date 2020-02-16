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


def goto_main():
    try:
        driver.refresh()
        Alert(driver).accept()
    except Exception as e:
        print(e)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '._2zCfw')))


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


def unread_user_names():
    time.sleep(5)
    scrolls = 100
    # driver.goto_main()
    initial = 10
    user_names = []
    for i in range(0, scrolls):
        driver.execute_script("document.getElementById('pane-side').scrollTop={}".format(initial))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for i in soup.find_all("div", class_="_2WP9Q"):
            if i.find("div", class_="_1ZMSM"):
                username = i.find("div", class_="_3H4MS").text
                user_names.append(username)
        initial += 10
    # Remove duplicates
    user_names = list(set(user_names))
    print(user_names)


def get_last_message_for():
    name = input("Enter name: ")
    messages = list()
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for i in soup.find_all("div", class_="FTBzM"):
        message = i.find("div", class_="_12pGw")
        if message:
            messages.append(message.text)
    messages = list(filter(None, messages))
    print(messages)


def send_picture():
    name = input("Enter name: ")
    caption = input("Enter a nice caption: ")
    picture_location = "/home/bolt/Pictures/201320.jpg"
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
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
    name = input("Enter name: ")
    document_location = "/home/bolt/Documents/file.pdf"
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


def get_status():
    name = input()
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    try:
        group_xpath = "/html/body/div/div/div/div[3]/header/div[1]/div/span/img"
        click_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, group_xpath)))
        click_menu.click()
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException:
        return "None"
    except Exception:
        return "None"
    try:
        status_css_selector = ".drawer-section-body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"  # This is the css selector for status
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, status_css_selector)))
        status = driver.find_element_by_css_selector(status_css_selector).text
        for i in range(10):
            if len(status) > 0:
                return status
            else:
                time.sleep(1)
        return "None"
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException:
        return "None"
    except Exception:
        return "None"


def get_last_seen():
    name = input()
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    last_seen_css_selector = "._315-i"
    start_time = dt.datetime.now()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, last_seen_css_selector)))
        while True:
            last_seen = driver.find_element_by_css_selector(last_seen_css_selector).text
            if last_seen and "click here" not in last_seen:
                return last_seen
            end_time = dt.datetime.now()
            elapsed_time = (end_time - start_time).seconds
            if elapsed_time > 10:
                return "None"
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException:
        return "None"
    except Exception:
        return "None"


def clear_chat(self, name):
    driver.find_element_by_css_selector("._2zCfw").send_keys(name + Keys.ENTER)
    menu_xpath = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/div/span"
    WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
        (By.XPATH, menu_xpath)))
    menu = driver.find_element_by_xpath(menu_xpath)
    menu.click()
    chains = ActionChains(driver)
    for i in range(4):
        chains.send_keys(Keys.ARROW_DOWN)
    chains.send_keys(Keys.ENTER)
    chains.perform()
    clear_xpath = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]'
    WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
        (By.XPATH, clear_xpath)))
    driver.find_element_by_xpath(clear_xpath).click()


def participants_count_for_group():
    group_name = input()
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(group_name + Keys.ENTER)
    try:
        click_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "._19vo_ > span:nth-child(1)")))
        click_menu.click()
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException as e:
        return "None"
    except Exception as e:
        return "None"
    current_time = dt.datetime.now()
    participants_selector = "div._2LSbZ:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"
    while True:
        try:
            participants_count = driver.find_element_by_css_selector(participants_selector).text
            if "participants" in participants_count:
                return participants_count
        except Exception as e:
            pass
        new_time = dt.datetime.now()
        elapsed_time = (new_time - current_time).seconds
        if elapsed_time > 10:
            return "NONE"


def get_group_participants():
    group_name = input()
    participants_count_for_group(group_name)
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(group_name + Keys.ENTER)
    try:
        click_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#main > header > div._1WBXd > div._2EbF- > div > span")))
        click_menu.click()
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException as e:
        return "None"
    except Exception as e:
        return "None"
    participants = []
    scrollbar = driver.find_element_by_css_selector(
        "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div")
    for v in range(1, 70):
        print(v)
        driver.execute_script('arguments[0].scrollTop = ' + str(v * 300), scrollbar)
        time.sleep(0.10)
        elements = driver.find_elements_by_tag_name("span")
        for element in elements:
            try:
                html = element.get_attribute('innerHTML')
                soup = BeautifulSoup(html, "html.parser")
                for i in soup.find_all("span", class_="_3TEwt"):
                    if i.text not in participants:
                        participants.append(i.text)
                        print(i.text)
            except Exception as e:
                pass
        elements = driver.find_elements_by_tag_name("div")
        for element in elements:
            try:
                html = element.get_attribute('innerHTML')
                soup = BeautifulSoup(html, "html.parser")
                for i in soup.find_all("div", class_="_25Ooe"):
                    j = i.find("span", class_="_1wjpf")
                    if j:
                        j = j.text
                        if "\n" in j:
                            j = j.split("\n")
                            j = j[0]
                            j = j.strip()
                            if j not in participants:
                                participants.append(j)
                                print(j)
            except Exception as e:
                pass
    return participants


def create_group(self, group_name, members):
    more = driver.find_element_by_css_selector(
        "#side > header > div._20NlL > div > span > div:nth-child(3) > div > span")
    more.click()
    chains = ActionChains(driver)
    chains.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
    chains.perform()
    for member in members:
        contact_name = driver.find_element_by_css_selector("._16RnB")
        contact_name.send_keys(member + Keys.ENTER)
    time.sleep(3)  # little delay to make the process robust
    next_step = driver.find_element_by_css_selector("._3hV1n > span:nth-child(1)")
    next_step.click()
    group_text = driver.find_element_by_css_selector(".bsmJe > div:nth-child(2)")
    group_text.send_keys(group_name + Keys.ENTER)


def join_group(self, invite_link):
    driver.get(invite_link)
    try:
        Alert(driver).accept()
    except:
        print("No alert Found")
    join_chat = driver.find_element_by_css_selector("#action-button")
    join_chat.click()
    WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]')))
    join_group = driver.find_element_by_xpath(
        '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]')
    join_group.click()


# This method is used to get an invite link for a particular group
def get_invite_link_for_group(self, groupname):
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(groupname + Keys.ENTER)
    driver.find_element_by_css_selector("#main > header > div._5SiUq > div._16vzP > div > span").click()
    try:
        # time.sleep(3)
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div > div > div:nth-child(5) > div:nth-child(3) > div._3j7s9 > div > div")))
        invite_link = driver.find_element_by_css_selector(
            "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div > div > div:nth-child(5) > div:nth-child(3) > div._3j7s9 > div > div")
        invite_link.click()
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
            (By.ID, "group-invite-link-anchor")))
        link = driver.find_element_by_id("group-invite-link-anchor")
        return link.text
    except:
        print("Cannot get the link")


# This method is used to exit a group


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.whatsapp.com/')
    # send_messages()
    # unread_user_names()
    # get_last_message_for()
    # send_picture()
    send_document()
    '''

    get_status()
    get_last_seen()
    clear_chat()
    participants_count_for_group()
    get_group_participants()
    create_group()
    join_group()
    get_invite_link_for_group()
    '''
