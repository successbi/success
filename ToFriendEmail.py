#author:subi
import requests,json,smtplib
from email.mime.text import MIMEText

#获取天气
def getWhether(city,link):
    url = link + city
    r = requests.get(url).json()
    msg = '\r\n亲爱的，今天的天气是'+r['data']['forecast'][0]['type'] + '\r\n温度：'+r['data']['forecast'][0]['' \
                                                                                                 'high']+'--'+r['data']['forecast'][0]['low']
    return str(msg)

#获取word
def getWord(link):
    r = requests.get(link).json()
    msg = '\r\n\r\n' + r['content'] + '\r\n' + r['note']
    return str(msg)

def send():

    data = {
        'link' : 'http://open.iciba.com/dsapi',
        'links' : 'http://wthrcdn.etouch.cn/weather_mini?city=',
        'city' : '广州',
        'first' :'您的小可爱上线了！\r\n',
        'last' : '\r\n\r\n                         最爱你的人儿、、、、'
    }

    #构造邮件结构
    msg = data['first']+getWhether(data['city'],data['links'])+getWord(data['link'])+data['last']
    message = MIMEText(msg)
    message['Subject'] = '亲爱的，请注意查收'
    message['From'] = '老毕'
    message['To'] = '大会'


    #发送
    try:
        s = smtplib.SMTP()
        s.connect('smtp.qq.com',25)
        s.login('870143604@qq.com','epuxbfmcdrnwbgaf')
        s.sendmail('870143604@qq.com','2353514708@qq.com',message.as_string())
        s.quit()

        print('done!!')
    except:
        send()

for i in range(10):
    send()