# coding:utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import globalparam
import logging

class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def scroll(self, n):
        logging.info("缓慢滑动当前页面{0}s".format(n*0.05))
        for i in range(n):
            self.driver.execute_script("document.body.scrollTop+=10")
            sleep(0.05)

    def type_and_tab(self, element, text):
        try:
            element.clear()
            logging.info("输入 {0}, 并按下TAB键".format(text))
            element.send_keys(text)
            element.send_keys(Keys.TAB)
        except Exception:
            logging.warning("输入 {0}, 并按下TAB键时出错".format(text))

    def type_and_enter(self, element, text):
        try:
            element.clear()
            logging.info("输入 {0}, 并按下ENTER键".format(text))
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
        except Exception:
            logging.warning("输入 {0}, 并按下ENTER键时出错".format(text))

    def login(self):
        try:
            self.type_and_tab(self.driver.find_element_by_name('username'), globalparam.username)
            self.type_and_enter(self.driver.find_element_by_name('password'), globalparam.password)
            logging.info("登录成功, username: {0}, password: {1}"
                         .format(globalparam.username, globalparam.password))
            sleep(2)
        except Exception:
            logging.warning("登录时出错, username: {0}, password: {1}"
                            .format(globalparam.username, globalparam.password))

    def move_to_element(self, element):
        try:
            ActionChains(self.driver).move_to_element(element).perform()
            logging.info("鼠标移动到{0}元素".format(element))
        except Exception:
            logging.warning("鼠标移动到{0}元素失败".format(element))

