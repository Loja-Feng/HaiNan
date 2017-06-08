# -*- encoding:utf-8 -*-
import re
from datetime import datetime
s=u'本院定于二○一七年二月十七日整在本院第四法庭公开审理原告海南德沣环保建材科技股份有限公司诉被告詹新阳、京鑫建设集团有限公司海南分公司买卖合同纠纷一案。'
#s=u'本院定于2017年2月17日在本院第二审判庭公开开庭审理原审被告人李孟觉等5人犯贪污罪即上诉、抗诉一案。'

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
    #s=s.split(u'定于', 1)[-1].split(u'在', 1)[0].split(u'日', 1)[0]
    pattern = re.compile(u'.{1,4}年.{1,3}月.{1,3}日(整)?在本院', re.I)
    s = pattern.search(s).group()
    year = s.split(u'年',1)[0]
    date_map[year[0]]
    year = date_map[year[0]]+date_map[year[1]]+date_map[year[2]]+date_map[year[3]]
    # return year
    month = s. split(u'年', 1)[-1].split(u'月',1)[0]
    if u'十' in month:
        month = '1' + date_map[month[-1]]
    else:
        month = date_map[month]
    day = s. split(u'月', 1)[-1].split(u'日',1)[0]
    if len(day) ==1 and u'十' not in day:
        day = date_map[day[0]]
    elif len(day) == 1 and u'十' in day:
        day =10
    elif len(day) ==2:
        if day[0] == u'十':
            day = '1'+ date_map[day[1]]
        else :
            day = date_map[day[0]]+date_map[day[1]]
    else:
        day = date_map[day[0]]+date_map[day[2]]
    # pattern = re.compile(u'\d{4}年\d{1,2}月\d{1,2}日',re.I)
    # s=pattern.search(s).group().replace(u'年', '-').replace(u'月', '-').replace(u'日', '')
    return '%s-%s-%s' % (year, month, day)

def time_format(s):
    pattern = re.compile(u'.{1,4}年.{1,3}月.{1,3}日(整)?在本院', re.I)
    s = pattern.search(s)
    if s:
        s = '0:00'
    else:
        s=s.split(u'定于', 1)[-1].split(u'在', 1)[0].split(u'日', 1)[-1]
        if u'上午' in s:
            if u'整'in s:
                s=s.split(u'午', 1)[-1].split(u'时整',1)[0].split(u'点整', 1)[0]
                # print s
                if len(s)==1 and u'十' not in s:
                    s=date_map[s]+':00'
                elif len(s)==1 and u'十' in s:
                    s='10'
                else:
                    s='1'+date_map[s[1]]+':00'
            else :
                s=s.split(u'午', 1)[-1].split(u'时',1)[0].split(u'点',1)[0]
                if len(s)==1 and u'十' not in s:
                    s=date_map[s]+':00'
                elif len(s)==1 and u'十' in s:
                    s='10'
                else:
                    s='1'+date_map[s[1]]+':00'
        elif u'下午' in s:
            if u'整'in s:
                s=s.split(u'午', 1)[-1].split(u'时整',1)[0].split(u'点整', 1)[0]
                if len(s)==1 and u'十' not in s:
                    s=str(12+int(date_map[s]))+':00'
                elif len(s)==1 and u'十' in s:
                    s='22'+':00'
                else:
                    s=str(22+int(date_map[s[1]]))+':00'
            else :
                s=s.split(u'午', 1)[-1].split(u'时',1)[0].split(u'点',1)[0]
                if len(s)==1 and u'十' not in s:
                    s=str(12+int(date_map[s]))+':00'
                elif len(s)==1 and u'十' in s:
                    s='22'+':00'
                elif len(s)==2 and u'十' in s:
                    s=str(22+int(date_map[s[1]]))+':00'
                elif len(s)==2 and u'十' not in s:
                    s=int(s)+':00' if int(s)>=12 else int(s) +'12'
        elif u'上午' or u'下午' not in s:
            print s
            hour = s.split(u'时',1)[0].split(u'点',1)[0]
            minute = s.split(u'时',1)[-1].split(u'点',1)[-1].replace(u'分', '')
            if len(hour)==1 and u'十' not in hour[0]:
                hour= date_map[hour[0]]
            elif len(hour)==1 and u'十'  in hour[0]:
                hour='10'
            elif len(hour)==2 and u'十' in hour[0]:
                hour= str(10+int(date_map[hour[1]]))
            elif len(hour)==2 and u'十' in hour[1]:
                hour=date_map[hour[0]]+date_map[hour[1]]
            elif len(hour)==3 and u'十' in hour[1]:
                hour =date_map[hour[0]]+date_map[hour[-1]]
            if len(minute)==0:
                minute='00'
            elif len(minute)==1 and u'十' not in minute[0] and u'零' not in minute[0]:
                minute= date_map[minute[0]]
            elif len(minute)==1 and u'十' not in minute[0] and u'零'  in minute[0]:
                minute ='00'
            elif len(minute)==1 and u'十'  in minute[0]:
                minute='10'
            elif len(minute)==2 and u'十' in minute[0]:
                minute= str(10+int(date_map[minute[1]]))
            elif len(minute)==2 and u'十' in minute[1]:
                minute=date_map[minute[0]]+date_map[minute[1]]
            elif len(minute)==3 and u'十' in minute[1]:
                minute =date_map[minute[0]]+date_map[minute[-1]]
            s=hour+':'+minute
    return s



date = date_format(s)
time = time_format(s)
at_date = datetime.strptime('%s %s' % (date, time), '%Y-%m-%d %H:%M') # at_date
print date
print time
print at_date
