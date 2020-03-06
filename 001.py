import datetime


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
    # 日期转字符串
    meeting_start = otherday.strftime('%Y-%m-%d %H:%M:%S')
    return meeting_start


def meeting_end():
    """
    :return: 会议开始
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=13)
    otherday = today + oneday
    # 日期转字符串
    # 日期转字符串
    meeting_end = otherday.strftime('%Y-%m-%d %H:%M:%S')
    return meeting_end




meeting_start=meeting_start()
enroll_start=enroll_start()
enroll_end=enroll_end()
meeting_end =meeting_end ()
print(meeting_end )
print(enroll_start)
print(enroll_end)
print(meeting_start)
print(type(meeting_end))
