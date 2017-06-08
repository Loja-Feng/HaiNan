# -*- encoding: utf-8 -*-
import re
#s='本院定于2017年5月22日 下午13时在塔洋法庭公开开庭审理原告许丽娟诉被告陈远新、陈廷进共有纠纷一案。'
#s='本院定于2017年5月24日 上午9时在本院新兴法庭公开开庭审理原告吴启胜与被告黄赞钦生命权、健康权、身体权纠纷一案。'
#s='本院定于2017年6月21日 下午3时在本院中法庭二公开开庭审理原告王啟柏与被告吴佰凤离婚纠纷一案。'
s=u'本院定于2017年03月06日上午 08:30在第九法庭公开审理北京永利源混凝土有限公司海南儋州分公司与亚太财产保险有限公司海南分公司财产保险合同纠纷一案。'
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
    s=s.split(u'定于',1)[-1].split(u'在')[0].split()[0]
    pattern = re.compile(ur'\d{1,4}年\d{1,2}月\d{1,2}日', re.I)
    s = pattern.search(s).group().replace(u'年', '-').replace(u'月', '-').replace(u'日', '')
    return s
def time_format(s):
    s=s.split(u'定于',1)[-1].split(u'在')[0].split()[-1]
    if u'上午' in s:
        pattern = re.compile(ur'(上午){1}\d{1,2}时',re.I)
        s = pattern.search(s).group().replace(u'上午','').replace(u'时',':00')
        return s
    else:
        pattern = re.compile(ur'(下午){1}\d{1,2}时',re.I)
        s = pattern.search(s).group().replace(u'下午','').replace(u'时','')
        s =  str(int(s)+12) if int(s)<=12 else s +':00'
        return s

date = date_format(s)
time = time_format(s)
print date
print time
