# encoding: utf-8
from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
from alert import DataInteg
import os
import psycopg2

def clean_data():
    print("Clear Test Date")
    db = os.environ["PG_DB"]
    user = os.environ["PG_USER"]
    passwd = os.environ["PG_PASSWORD"]
    host = os.environ["PG_HOST"]
    port = os.environ["PG_PORT"]
 
    #创建连接对象
    conn = psycopg2.connect(database=db, user=user, password=passwd, host=host, port=port)
    cur = conn.cursor() #创建指针对象   
    #删除数据
    cur.execute("DELETE FROM meetings WHERE name LIKE %s",('AUTOTEST_%',))
    cur.execute("DELETE FROM organs WHERE phone LIKE %s",('190%',))
    # 关闭连接
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    print("Start....")
    runner = HttpRunner(failfast=False)

    #执行测试用例集
    summary = runner.run('./testsuites')
    #生成报告
    gen_html_report(summary)
    #清理测试数据
    clean_data()
    #推送钉钉消息
    #DataInteg.genHtml(summary)
    print("End....")
