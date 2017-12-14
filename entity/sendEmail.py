import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'answer_sky13@163.com'
receivers = ['2048875230@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送...可以测试了', 'plain', 'utf-8')
message['From'] = "answer_sky13@163.com"
message['To'] = "916323118@qq.com"

subject = 'asaas'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.163.com')  # 25 为 SMTP 端口号
    smtpObj.login("answer_sky13@163.com", "answer2017")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")