import os
import random
import datetime
import alert
import  psycopg2

def gen_name():
    val = random.randint(0x4e00, 0x9fbf)
    return "AUTOTEST_"+chr(val)+chr(val)


def gen_contact():
    val = random.randint(0x4e00, 0x9fbf)
    return "AUTOTEST_"+chr(val)


def gen_mobile():
    prelist=["190"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))


def hook_print(any):
    print(any)


def enroll_start():
    """
    :return: 报名开始日期
    """
    today = datetime.date.today()
    # 日期转字符串
    enroll_start=today.strftime('%Y-%m-%d %H:%M:%S')
    return enroll_start

def enroll_end():
    """
    :return: 报名结束日期
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=7)
    otherday = today + oneday
    # 日期转字符串

    enroll_end = otherday.strftime('%Y-%m-%d %H:%M:%S')
    return enroll_end

def meeting_start():
    """
    :return: 会议开始
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=10)
    otherday = today + oneday
    # 日期转字符串

    meeting_start = otherday.strftime('%Y-%m-%d %H:%M:%S')
    return meeting_start


def meeting_end():
    """
    :return: 会议结束
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=17)
    otherday = today + oneday
    # 日期转字符串
    # 日期转字符串
    meeting_end = otherday.strftime('%Y-%m-%d %H:%M:%S')
    return meeting_end


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
    cur.execute("DELETE FROM organs WHERE name LIKE %s",('190%',))
 
    # 关闭连接
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    hook_print("It's working.")