#Python 网易邮箱简单发送邮件
# -*- coding: utf-8 -*-


import smtplib  # 导入PyEmail
from email.mime.text import MIMEText
import sys
sys.path.append('./')
from util.fileDeal import  get_email
email_dict = get_email()["email"]

# 邮件构建

def send(msg):
    subject = "收益！"  # 邮件标题
    sender = email_dict["user"]  # 发送方
    content = msg
    recver = email_dict["user"]  # 接收方
    password = email_dict["pwd"] #邮箱密码
    message = MIMEText(content, "plain", "utf-8")
    # content 发送内容     "plain"文本格式   utf-8 编码格式
    message['Subject'] = subject  # 邮件标题
    message['To'] = recver  # 收件人
    message['From'] = sender  # 发件人
    smtp = smtplib.SMTP_SSL(email_dict["server"], 994)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()



if __name__=='__main__':
    send("11")
        