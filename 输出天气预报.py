# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/3 16:21
data={'1396797251':666666,'1443008472':777777}
qq=input('请输入qq号登陆:')
passwaord=input('密码:')
for a in data:
    if  qq!=a and passwaord !=data[a]:
        print('账号或者密码错误')
    else:
        print('登录成功')
        break
