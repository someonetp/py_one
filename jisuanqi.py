# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/5 17:00

def caculeite(a,b,c):
    if c=='+':
        return  a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        if b != 0:
            return a / b
        else:
            print('输入错误，分母不能为零')




if __name__ == '__main__':
    a=caculeite(20,10,'/')
    print(a)