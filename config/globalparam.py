# coding:utf-8
from configparser import ConfigParser
import time
import logging

config = ConfigParser()
config.read('f:/webUI_automation/config/config.ini', encoding='utf-8')

username = config.get('info', 'username')
password = config.get('info', 'password')
domain = config.get('info', 'domain')
f_path = config.get('info', 'path')

case_list = []
case_all = config.options('testcases')
for case in case_all:
    if config.getint('testcases', case):
        case_list.append(case)
case_list = map(lambda x: 'testcases.' + x, case_list)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=f_path+'/log/log'+time.strftime('%Y%m%d%H%M%S', time.localtime())+'.txt',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

is_sendmail = config.getint('email', 'is_sendmail')
e_recvaddress = config.get('email', 'recvaddress')
e_sendaddr_name = config.get('email', 'sendaddr_name')
e_sendaddr_pswd = config.get('email', 'sendaddr_pswd')