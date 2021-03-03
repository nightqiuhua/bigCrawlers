from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(to_addr,title,msg_body):
    """发送邮件
    @param to_addr 字符串 发件人
           title   字符串 邮件主题
           msg_body 字符串 邮件信息
 
    """

    host = 'smtp.163.com'  
    # 设置发件服务器地址
    port = 465  
    # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
    sender = 'caimouqiu@163.com'  
    # 设置发件邮箱，一定要自己注册的邮箱
    pwd = 'olcwkwhjrxj22'  
    # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
    body = msg_body
    # 设置邮件正文，这里是支持HTML的
    msg = MIMEText(msg_body, 'html') 
    # 设置正文为符合邮件格式的HTML内容
    msg['subject'] =title
    # 设置邮件标题
    msg['from'] = sender  
    # 设置发送人
    msg['to'] = to_addr  
    # 设置接收人
    try:
        s = smtplib.SMTP_SSL(host, port)  
        # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)  
        # 登陆邮箱
        s.sendmail(sender, to_addr, msg.as_string())
        # 发送邮件！
        print ('Done.sent email success')
    except smtplib.SMTPException:
        print ('Error.sent email fail')
