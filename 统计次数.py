# 教育机构 ：
# 使用人 ：付佳诚
# 开发时间：2022/9/5 15:10
def get_cout(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


if __name__ == '__main__':
    s = 'hello python. i love python and python will be population forever'
    o = input('请输入要统计的字符:')
    count = get_cout(s, o)
    print(f'o 在{s}中出现的次数:{count}')
