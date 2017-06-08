# -*- encoding:utf-8 -*-
import re
from datetime import datetime
#s=u' 本院定于二○一七年五月二十五日上午九时整在本院第五法庭公开审理被告人黄钦意贩卖毒品一案。'
#s=u'本院定于二○一七年五月二十五日下午十一时整在本院第三法庭公开审理原告海南耀兴运输集团有限公司旅游客运分公司诉被告黄燕劳动争议纠纷一案。'
#s=u' 本院定于二〇一七年五月十七日十时零分在本院科技法庭公开审理被告人黎铭柳贩卖毒品一案。'
#s=u'本院定于二〇一七年五月十七日二十一时四十分在本院科技法庭公开审理被告人黎铭柳贩卖毒品一案。'
#s=u'本院定于二○一七年五月二十三日上午九时整在本院第五法庭公开审理被告人雷青山贩卖毒品一案。'
#s=u'本院定于二○一七年三月八日下午三时整在本院第五法庭公开审理被告人陈志挪用公款、贪污一案。'
#s=u'本院定于二○一七年三月七日上午九时整在本院第四法庭公开审理原告刘观荣；邱湘坚诉被告海南海石工贸公司、海口深琼长安实业有限公司、海口安得物业管理有限公司房屋买卖合同纠纷一案。'
#s=u'　本院定于2017年01月6日上午9时在本院第五法庭公开开庭审理夏明春与李绍胜、李东豪、黎振章、王位钰、李绍义、吴多丰、黎振均、凌家浩、李绍宇、王崇滨侵权责任纠纷一案。'
#s=u'本院定于二○一七年三月九日上午九时整在本院第一法庭公开审理原告陈僚诉被告海南鸿利来地产开发有限公司房屋买卖合同纠纷一案。'
#s=u'本院定于2017年3月21日下午14:30在第五法庭公开开庭审理原告：三亚致远物业服务有限公司诉被告：胡宛抒物业服务合同纠纷一案。'
#s=u'本院定于2017年3月23日下午14:30在第三法庭公开开庭审理被告人：符道耀、王亚保涉嫌犯盗窃罪一案。'
#s=u'本院定于2017年3月21日下午14:30在第五法庭公开开庭审理原告：三亚致远物业服务有限公司诉被告：姚承洪物业服务合同纠纷一案。'
#s=u'本院定于2017年3月6日下午14:30于第六法庭公开开庭审理原告：三亚致远物业服务有限公司诉被告：张旭物业服务合同纠纷一案。'
#s=u'本院定于2017年3月6日下午14:30于第六法庭公开开庭审理原告：三亚致远物业服务有限公司诉被告：王连存物业服务合同纠纷一案。'
#s=u'本院定于二○一七年二月二十七日上午九点整在本院第五法庭公开审理被告人韩健诈骗一案。'
#s=u'本院定于二○一七年二月十日上午九时整在本院家事法庭公开审理原告王杨斌诉被告王录清离婚纠纷一案。'
#s=u'本院定于二零一六年四月二十八日九时  在万宁市人民法院第二审判庭，依法公开宣判被告人吴乾国故意伤害罪一案。'
#s=u'本院定于 2016 年 5 月 30 日下午 15 时在本院第三审判庭，依法公开审理原告万宁市农村信用合作联社诉被告文亚和、林淑春金融借款合同纠纷一案'
#s=u'本院定于2016年10月19日15时45分在本院第三审判庭，依法公开审理原告中国农业银行股份有限公司万宁市支行与被告李本祝、陈春梅、陈春月金融借款合同纠纷一案'
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
    s=''.join(s.split())
    pattern = re.compile(u'.{1,4}年.{1,3}月.{1,3}(日)?',re.I)
    s = pattern.search(s).group()
    year = s.split(u'年',1)[0]
    date_map[year[0]]
    year = date_map[year[0]]+date_map[year[1]]+date_map[year[2]]+date_map[year[3]]
    # return year
    month = s. split(u'年', 1)[-1].split(u'月',1)[0]
    if u'十' in month:
        month = '1' + date_map[month[-1]]
    elif len(month)==1:
        month = date_map[month[0]]
    elif len(month)==2 and '0' not in month[0]:
        month = '1'+date_map[month[-1]]
    elif len(month)==2 and '0' in month[0]:
        month = date_map[month[-1]]
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
    s=''.join(s.split())
    s=s.split(u'定于', 1)[-1].split(u'在', 1)[0].split(u'日', 1)[-1]
    if u'上午' in s:
        if u'整'in s:
            s=s.split(u'午', 1)[-1].split(u'时整',1)[0].split(u'点整', 1)[0]
            if len(s)==1 and u'十' not in s:
                s=str(12+int(date_map[s]))+':00'
            elif len(s)==1 and u'十' in s:
                s='10'
            else:
                s='1'+date_map[s[1]]+':00'
        else :
            s=s.split(u'午', 1)[-1].split(u'时',1)[0].split(u'点',1)[0]
            if len(s)==1 and u'十' not in s:
                s=str(12+int(date_map[s]))+':00'
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
            print s
            if len(s)==1 and u'十' not in s:
                s=str(12+int(date_map[s]))+':00'
            elif len(s)==1 and u'十' in s:
                s='22'+':00'
            elif len(s)==2 and u'十' in s:
                s=str(22+int(date_map[s[1]]))+':00'
            elif len(s)==2 and u'十' not in s:
                s=s+':00' if int(s)>=12 else s +'12'
    elif u'上午' or u'下午' not in s:
        # print s
        hour = s.split(u'时',1)[0].split(u'点',1)[0].strip()
        minute = s.split(u'时',1)[-1].split(u'点',1)[-1].replace(u'分', '').strip()
        # print len(minute)
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
            minute ='00'
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

date=date_format(s).strip()
time=time_format(s).strip()
#at_date = datetime.strptime('%s %s' % (date, time), '%Y-%m-%d %H:%M') # at_date
print date
print time
print at_date
