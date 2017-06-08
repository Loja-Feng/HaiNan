# -*- encoding: utf-8 -*-
import re
s=u'本院定于2017年5月25日下午15:00在第五法庭公开开庭审理原告黄坤姑诉被告崔梦琳租赁合同纠纷一案。'
def date_format(s):
    s = s.split(u'定于', 1)[-1].split(u'在', 1)[0]
    pattern = re.compile(ur'\d{1,4}年\d{1,2}月\d{1,2}日')
    s = pattern.search(s).group().replace(u'年','-').replace(u'月', '-').replace(u'日','')
    return s
def time_format(s):
    pattern = re.compile(ur'\d{1,4}年\d{1,2}月\d{1,2}日')
    s = s.split(u'定于', 1)[-1].split(u'在', 1)[0]
    if u'上午' in s:
        s = s.split(u'上午',1)[-1]
        pattern = re.compile(ur'\d{1,2}:\d{1,2}')
        s = pattern.search(s).group()
    else:
        s = s.split(u'下午',1)[-1]
        pattern = re.compile(ur'\d{1,2}:\d{1,2}')
        s = pattern.search(s).group().replace(s.split(':',1)[0],str(int(s.split(':',1)[0])+12) if int(s.split(':',1)[0])<=12 else s.split(':',1)[0])
    return s
date = date_format(s)
time = time_format(s)
print date
print time
