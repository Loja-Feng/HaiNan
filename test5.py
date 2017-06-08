# -*- encoding:utf-8 -*-
import re
#s=u'本院定于2017年03月06日上午 08:30在第九法庭公开审理北京永利源混凝土有限公司海南儋州分公司与亚太财产保险有限公司海南分公司财产保险合同纠纷一案。'
#s=u'本院定于2017年02月28日下午16：30在第二法庭公开审理海南名都物业服务有限公司与何姬物业服务合同纠纷一案。'
#s=u'本院定于2017年02月27日上午10：30在第九法庭公开审理海南名都物业服务有限公司与林一雄物业服务合同纠纷一案。'
s=u'本院定于2017年3月3日下午15;00在第五法庭公开审李玉莲诉苏焕文、钟翠燕民间借贷纠纷一案。'
def date_format(s):
    pattern = re.compile(ur'\d{1,4}年\d{1,2}月\d{1,2}日.{1,2}',re.I)
    date = pattern.search(s).group().split(u'日',1)[0].replace(u'年', '-').replace(u'月', '-')
    return date

def time_format(s):
    pattern = re.compile(ur'\d{1,4}年\d{1,2}月\d{1,2}日.{2}.+\d{1,2}[:|：|;]\d{1,2}', re.I)
    time = pattern.search(s).group().split(u'午',1)[-1].split()[-1].replace(u'：',':').replace(u';',':')
    return time
date = date_format(s)
time = time_format(s)
print date
print time
