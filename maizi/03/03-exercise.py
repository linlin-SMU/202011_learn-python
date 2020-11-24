# '''6公里以内 3元
# （6,12】 4元
# （12,22】 5元
# （22， 32】 6元
# 100元
# （100,150】 8折
# （150,400】 5折
# （400， '''
#
# lenth1 = input('请输入每天的公里数： ')
# each_lenth = int(lenth1)
# if each_lenth < 6:
#     each_money = 3
# elif 6< each_lenth <= 12:
#     each_money = 4
# elif 12< each_lenth <=22:
#     each_money = 5
# else:
#     each_money = 6
# day_money = each_money * 2
# month_money = day_money * 20
# if month_money <= 100:
#     final_money = month_money
# elif 100 < month_money <= 150:
#     final_money = (month_money-100) * 0.8 + 100
# elif 150 < month_money <= 400:
#     final_money = (month_money - 150) * 0.5 + 50 * 0.8 + 100
# else:
#     final_money = (month_money-400) + 250 * 0.5 + 50 * 0.8 + 100
# print('本月花费：%.d 元。' % final_money)
#

mystr = '01234'
print(mystr[-2:-1])  # [-2,-1) 其中4为-1
print(mystr[::-1])  # 倒数方向截取
print(mystr[::2])   # 起始截一个，空一个，截取一个