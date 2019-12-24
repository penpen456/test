"""
查找某字符出现的次数与位置
"""

t = 0
string = input('输入字符串: ')
keyword = input('输入查找的字符: ')
print('查找结果如下：'.center(27, '-'))
count = string.count(keyword)
print('{0}字符出现的次数为: {1}'.format(keyword, count))
for i in range(count):
    pos = string.find(keyword, t)
    print('{0}字符出现的位置为: {1}'.format(keyword, pos))
    t = pos + 1
