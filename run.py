# encoding: utf-8
from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
from alert import DataInteg

runner = HttpRunner(failfast=False)

#执行测试用例集
summary = runner.run('./testsuites')
#生成报告
gen_html_report(summary)
#推送钉钉消息
DataInteg.genHtml(summary)