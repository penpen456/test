# 生成一个大文件
# with open('./big.txt', 'w') as f:
#     f.seek(1*1024*1024*1024)
#     f.write('end')
with open('./big.txt') as f:
    t = f.read(100000000)
    print(t)
