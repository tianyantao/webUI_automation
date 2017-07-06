# coding:utf-8
import basepage
from config import globalparam
import logging
from time import sleep

class TeacherPage(basepage.Page):

    def to_study_record_page(self):
        try:
            self.driver.find_element_by_xpath('//a[@href="/teacher"]').click()
            logging.info("进入学习记录页面")
        except Exception:
            logging.warning("进入学习记录页面失败")

    def to_homework_detail_page(self):
        try:
            self.driver.find_element_by_xpath('//a[@href="/teacher/homework"]').click()
            logging.info("进入作业详情页面")
        except Exception:
            logging.warning("进入作业详情页面失败")

    def to_video_homework_page(self):
        try:
            basepage.Page(self.driver).move_to_element(self.driver.find_element_by_xpath('//li[@class="iconfont003"]'))
            sleep(1)
            self.driver.find_element_by_xpath('//a[@href="/teacher/homework/videoassignment"]').click()
            logging.info("进入视频作业页面")
        except Exception:
            logging.warning("进入视频作业页面失败")






