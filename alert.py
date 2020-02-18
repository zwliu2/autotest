import requests
import json

access_token = 'd54fd978ea84b3e43654bdff63e63213d8ba24c70eaaee013cacfcb5071d37d8'
project_name = '会议系统meeting'

class SendAlert:
    
    def send_alert(self):
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        send_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "自动化测试",
                "text": "#### API测试 \n" +
                    "> 项目名称: {}\n\n".format(project_name) +
                    "> api路径: {}\n\n".format('xxxxx') +
                    "> 测试结果: {}\n\n".format('ok') + 
            }
        }
        print(send_data)
        url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token)
        req = requests.post(url=url, data=json.dumps(send_data).encode('utf-8'), headers=headers)
        result = req.json()

        if result['errcode'] != 0:
            print('notify dingtalk error: %s' % result['errcode'])