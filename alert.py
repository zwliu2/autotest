import requests
import json, subprocess
import os

access_token = 'd54fd978ea84b3e43654bdff63e63213d8ba24c70eaaee013cacfcb5071d37d8'
project_name = '会议系统meeting'
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
    def genHtml(self, summary):
        file_lst = []
        for filename in os.listdir(absdir + '/' + 'reports'):
            if 'html' in filename:
                file_lst.append(filename)
                dir_name = filename.split('T')[0]
                command_lst = []
                command_lst.append("ssh runner@123.56.165.90 mkdir -p /files/data/zwinstall/{}/{}".format(tag, dir_name))
                command_lst.append("scp reports/{} runner@123.56.165.90:{}".format(filename, '/files/data/zwinstall/{}/{}'.format(tag, dir_name)))
                ConnRemoteHost().toHost(command_lst)

        SendAlert().send_alert(file_lst, summary)

class SendAlert:
    
    def send_alert(self, file_lst, summary):
        base_url = 'https://zwinstall.gugud.com/{}/'.format(tag)
        report_url = ''
        for x in file_lst:
            report_url = base_url + x.split('T')[0] + '/' + x + "   " + report_url
        headers = {'Content-Type': 'application/json;charset=utf-8'}

        # send_data = {
        #     "msgtype": "markdown",
        #     "markdown": {
        #         "title": "会议系统",
        #         "text": "#### API自动化测试【"+Util.result_str(summary['success'])+"】 \n" +
        #             "> 项目名: {}\n\n".format(project_name) +
        #             "> 接口访问地址: {}\n\n".format(os.getenv('API_URL')) + 
        #             "> 接口仓库地址: {}\n\n".format(os.getenv('CI_PROJECT_URL')) +
        #             "> 测试报告地址: {}\n\n".format(report_url)
        #     }
        # }
        send_data = {
            "msgtype": "text",
            "text": {
                "content": Util.result_str(summary['success'])+
                    "项目名: {}\n\n".format(project_name) +
                    "接口访问地址: {}\n".format(os.getenv('API_URL')) + 
                    "接口仓库地址: {}\n".format(os.getenv('CI_PROJECT_URL')) +
                    "测试报告地址: {}\n".format(report_url)
            }
        }
        url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token)
        req = requests.post(url=url, data=json.dumps(send_data).encode('utf-8'), headers=headers)
        result = req.json()

        if result['errcode'] != 0:
            print('notify dingtalk error: %s' % result['errcode'])

    
class Util:
    
    def result_str(result):
        if(result):
            return  "【通过】 API自动化测试"
        else:
            return  "==========================\n"+ 
                    "！！【失败】 API自动化测试！！"+
                    "==========================\n"