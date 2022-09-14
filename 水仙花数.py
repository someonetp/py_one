# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/5 11:16
import math
for a in range(100,1000):
    if a==math.pow((a%10),3)+math.pow((a//10%10),3)+math.pow((a//100),3):
        print(f'水仙花数是{a}')