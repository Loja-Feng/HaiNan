# -*- encoding:utf-8 -*-
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
#s=u'本院定于2017年5月22日下午14:30在第六法庭公开开庭审理原告包修源诉被告东方蓝城房地产开发有限公司商品房销售合同纠纷一案。'
s=u'本院定于2017年3月6日下午14:30于第六法庭公开开庭审理原告：三亚致远物业服务有限公司诉被告：张旭物业服务合同纠纷一案。'
#s=u'本院定于2017年2月28上午08：30在第五法庭公开开庭审理原告陈峰诉被告中海石油化学股份有限公司、中海油能源发展股份有限公司海南人力资源服务分公司劳动争议一案。'

date_map = {u'一' : '1',
            u'二' : '2',
            u'三' : '3',
            u'四' : '4',
            u'五' : '5',
            u'六' : '6',
            u'七' : '7',
            u'八' : '8',
            u'九' : '9',
            u'十' : '0',
            u'〇' : '0',
            u'o'  : '0',
            u'O'  : '0',
            u'零' : '0',
            u'○'  : '0',
            '0':'0',
            '1':'1',
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9'
}
def date_format(s):
    # s=s.split(u'定于', 1)[-1].split(u'在', 1)[0]
    # return s
    pattern = re.compile(u'\d{1,4}年\d{1,2}月\d{1,2}(日)?.{1}午\d{1,2}[:|：|；|;]\d{1,2}',re.I)
    s=pattern.search(s).group()
    pattern = re.compile(u'\d{1,4}年\d{1,2}月\d{1,2}',re.I)
    s = pattern.search(s).group().replace(u'年', '-').replace(u'月','-')
    return s

def time_format(s):
    pattern = re.compile(u'\d{4}年\d{1,2}月\d{1,2}(日)?.{1}午\d{1,2}[:|：|；|;]\d{1,2}',re.I)
    s=pattern.search(s).group()
    pattern = re.compile(u'\d{1,2}[:|：|；|;]\d{1,2}',re.I)
    s = pattern.search(s).group()
    return s

date=date_format(s)
time=time_format(s)
print date
print time
