import requests
import json, subprocess

access_token = 'd54fd978ea84b3e43654bdff63e63213d8ba24c70eaaee013cacfcb5071d37d8'
project_name = 'meeting'
tag = 'p0001-meeting'

class ConnRemoteHost:
    
    @classmethod
    def toHost(cls, command):
        for x in command:
            result = subprocess.Popen(x, shell=True, stdout=subprocess.PIPE)
            if result.stdout.readlines():
                for line in result.stdout.readline():
                    print(line)

class DataInteg:

    @classmethod
    def genHtml(self, data):
        filename = data['name']
        dir_name = data['name'].split('T')[0]
        command_lst = []
        command_lst.append("ssh runner@123.56.165.90 mkdir -p /files/data/zwinstall/{}/{}".format(tag, dir_name))
        command_lst.append("scp {} runner@123.56.165.90:{}".format(filename, '/files/data/zwinstall/{}/{}'.format(tag, dir_name)))
        ConnRemoteHost().toHost(command_lst)

        SendAlert().send_alert(data)

class SendAlert:
    
    def send_alert(self, data):
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        send_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "auto-test",
                "text": "#### API Test \n" +
                    "> project Name: {}\n\n".format(project_name) +
                    "> api url: {}\n\n".format('xxxxx') +
                    "> report url {}\n\n".format('https://zwinstall.gugud.com/{}/{}/{}'.format(tag, data['name'].split('T')[0], data['name']))
            }
        }
        print(send_data)
        url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token)
        req = requests.post(url=url, data=json.dumps(send_data).encode('utf-8'), headers=headers)
        result = req.json()

        if result['errcode'] != 0:
            print('notify dingtalk error: %s' % result['errcode'])


data = {
    'name': '20200218T085952.377442.html'
}
# DataInteg.genHtml(data) 场景测试执行完后调用此方法