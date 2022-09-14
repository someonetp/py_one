# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/3 16:10
'''第一种方式'''
fp=open('D:/test.txt','a+')
print('成就更好的自己',file=fp)

'''第二种写入方式'''
fp.close()
with open('D:/tees.txt','a+' )as file:
    file.write('自己是最棒的')