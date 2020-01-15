"""
用自己的方法将列表变成迭代器
"""

class MyIter:
    def __init__(self, test_list):
        self.test_list = test_list
        self.i = 0

    # 实现了这个方法我就是可迭代对象(能用for循环)
    def __iter__(self):
        return self       # 必须返回一个迭代器

    def __next__(self):
        try:
            t = self.test_list[self.i]              # 有了__next__魔法方法，我就是迭代器
        except IndexError:
            raise StopIteration
        else:
            # self.i += 1
            self.i += 2    # 调整步长为2
            return t


me = MyIter([1, 2, 3, 4])
# iter(me)       # iter()BIF会触发魔法方法__iter__()
for i in me:
    print(i)


"""
1.可迭代对象内部只实现了__iter__或者__getitem__方法
2.迭代器内部实现了__iter__和__next__方法
3.__iter__或者__getitem__方法必须返回迭代器
4.__next__方法是真正实现逻辑的地方
5.iter()BIF触发魔法方法__iter__或者__getitem__
6.next()BIF触发魔法方法__next__
7.从for循环看上面,for循环的原理：
  （1）a = iter(xxx),此时会调用__iter__方法,因为后面要用next(),所以必须要返回迭代器
  （2）next(a), 调用迭代器的__next__方法,实现逻辑,达到边界，抛出stop..error
  （3）接收stop..error


8.为什么要写自己的迭代器？？
   1.可以随意调整列表等序列的迭代规则，如迭代步长为2等等---因为默认列表等序列执行iter()后返回的迭代器的__next__都是步长为1
   2.当然range()可以修改步长，但一般的序列在for循环时不能修改
"""
