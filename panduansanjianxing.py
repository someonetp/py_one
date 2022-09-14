# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/5 17:25
def panduan(a, b, c):
    if a + b > c and a + c > b and b + c > a :
        print(f'{a} {b} {c}可以构成三角形')
    else:
        print('输入错误')


if __name__ == '__main__':
    print('请分别输入三角形的三边')
    a = int(input('第一边:'))
    b = int(input('第二边:'))
    c = int(input('第三边:'))
    sjx = panduan(a, b, c)
    print(sjx)
