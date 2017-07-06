# coding:utf-8
import unittest
import time
from config.globalparam import case_list
from config.globalparam import is_sendmail
from tools import HTMLTestRunner
from tools import sendmail
import logging


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromNames(case_list)
    logging.info('待执行测试用例集为：%s', case_list)
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    with open("./report/result" + now + ".html", 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report', description='Result:')
        runner.run(suite)
    if is_sendmail:
        time.sleep(3)
        mail = sendmail.SendMail()
        mail.send()
