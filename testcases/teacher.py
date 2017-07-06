# coding:utf-8
import logging
from config import globalparam
from pages import basepage
from pages import teacherpage
from selenium import webdriver
import unittest
from time import sleep

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("http://teacher.233.mistong.com")

    def tearDown(self):
        self.browser.close()
        self.browser.quit()

    def test_01(self):
        basepage.Page(self.browser).login()
        sleep(2)
        basepage.Page(self.browser).scroll(30)
        teacherpage.TeacherPage(self.browser).to_video_homework_page()
        sleep(2)
        try:
            self.assertIsNotNone(self.browser.find_element_by_xpath('//*[text()="请选择科目"]'))
            logging.info("断言成功")
        except AssertionError:
            logging.warning("断言失败，未找到元素")
        sleep(2)