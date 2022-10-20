import dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

dotenv.load_dotenv(dotenv.find_dotenv())
PATH = os.getenv("PATH0")
USER = os.getenv("USER")
SENHA = os.getenv("SENHA")
HASHTAG = os.getenv("HASHTAG")


class FacebookBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=PATH)

    # //input[@name="username"]
    #

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        user_element = driver.find_element(By.NAME, 'username')
        user_element.clear()
        user_element.send_keys(self.username)
        pass_element = driver.find_element(By.NAME, 'password')
        pass_element.clear()
        pass_element.send_keys(self.password)
        pass_element.send_keys(Keys.RETURN)
        time.sleep(5)
        box_element = driver.find_element(By.XPATH, '//button[@class="_a9-- _a9_1"]')
        box_element.send_keys(Keys.RETURN)
        self.curtirFotos(HASHTAG)

    def curtirFotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        hrefs = driver.find_element(By.TAG_NAME, 'a')
        hrefs.send_keys(Keys.RETURN)
        time.sleep(2)
        next = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button//span//*[name()='svg' and @aria-label='Next']")))
        for i in range(0,20):
            like = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button//span//*[name()='svg' and @aria-label='Like']"))).click()
            next.click()
            time.sleep(19)




ChesterBot = FacebookBot(USER, SENHA)
ChesterBot.login()
