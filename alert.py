import requests
import json, subprocess
import os

access_token = 'd54fd978ea84b3e43654bdff63e63213d8ba24c70eaaee013cacfcb5071d37d8'
project_name = 'meeting'
tag = 'p0001-meeting'
absdir = os.path.abspath(os.path.dirname(__file__))


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
    def genHtml(self):
        file_lst = []
        for filename in os.listdir(absdir + '/' + 'reports'):
            if 'html' in filename:
                file_lst.append(filename)
                dir_name = filename.split('T')[0]
                command_lst = []
                command_lst.append("ssh runner@123.56.165.90 mkdir -p /files/data/zwinstall/{}/{}".format(tag, dir_name))
                command_lst.append("scp {} runner@123.56.165.90:{}".format(filename, '/files/data/zwinstall/{}/{}'.format(tag, dir_name)))
                ConnRemoteHost().toHost(command_lst)

        SendAlert().send_alert(file_lst)

class SendAlert:
    
    def send_alert(self, file_lst):
        base_url = 'https://zwinstall.gugud.com/{}/'.format(tag)
        report_url = ''
        for x in file_lst:
            report_url = base_url + x.split('T')[0] + '/' + x + "   " + report_url
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        send_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "auto-test",
                "text": "#### API Test \n" +
                    "> project Name: {}\n\n".format(project_name) +
                    "> api interface url: {}\n\n".format(os.getenv('API_URL')) + 
                    "> gitlab url: {}\n\n".format(os.getenv('CI_PROJECT_URL')) +
                    "> report url {}\n\n".format(report_url)
            }
        }
        url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token)
        req = requests.post(url=url, data=json.dumps(send_data).encode('utf-8'), headers=headers)
        result = req.json()

        if result['errcode'] != 0:
            print('notify dingtalk error: %s' % result['errcode'])