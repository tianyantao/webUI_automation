# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import globalparam
import logging

# 测试报告的路径
reportPath = globalparam.f_path + '/report'
# 配置收发件人
recvaddress = eval(globalparam.e_recvaddress)

sendaddr_name = globalparam.e_sendaddr_name
sendaddr_pswd = globalparam.e_sendaddr_pswd


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        logging.info('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp.exmail.qq.com', 25)
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logging.info("发送邮件成功")
        except Exception:
            logging.error('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()


