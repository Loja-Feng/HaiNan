# -*-encoding:utf-8 -*-
import re
s=u'本院定于2017年02月27日上午10在第九法庭公开审理海南名都物业服务有限公司与王洁物业服务合同纠纷一案。'
def date_format(s):
    pattern = re.compile(u'\d{1,4}年\d{1,2}月\d{1,2}日.{1}午\d{1,2}', re.I)
    date = pattern.search(s).group().split(u'日',1)[0].replace(u'年', '-').replace(u'月', '-')
    return date

def time_format(s):
    pattern = re.compile(u'\d{1,4}年\d{1,2}月\d{1,2}日.{1}午\d{1,2}', re.I)
    time = pattern.search(s).group().split(u'午', 1)[-1]+':00'
    return time

date = date_format(s)
time = time_format(s)

print date
print time
