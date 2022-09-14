# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/5 10:53
for a in range(1,4):
    name=input('请输入用户名:')
    password=input('请输入密码:')
    if name=='马彪'and password=='666666':
        print('登录成功')
        break
    else:
        print('密码或账号错误，请重新输入')
        if  a<3:
            print(f'你还有{3-a}次机会')
else:
    print('输入次数以达到上限')
