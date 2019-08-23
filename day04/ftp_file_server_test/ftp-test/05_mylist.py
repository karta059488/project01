# 练习:
#   实现两个自定义列表相加:
#     class MyList:
#         def __init__(self, iterable):
#             self.data = list(iterable)
#         .... 以下自己实现

#     L1 = MyList([1, 2, 3])
#     L2 = MyList([4, 5, 6])
#     L3 = L1 + L2
#     print(L3)  # MyList([1,2,3,4,5,6])
#     L4 = L2 + L1
#     print(L4)  # MyList([4,5,6,1,2,3])
#     L5 = L1 * 2
#     print(L5)  # MyList([1,2,3,1,2,3])

class MyList:
    def __init__(self, iterable):
        print('__init__被调用')
        self.data = list(iterable)


    def __add__(self,rhs):
        print('__add__被调用')
        return MyList(self.data + rhs.data)

    def __mul__(self,rhs):
        print('__mul__被调用')
        return MyList(self.data * rhs)   # rhs 绑定整数

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __rmul__(self, lhs):
        print('__rmul__被调用')
        return MyList(self.data * lhs)

    def __iadd__(self,rhs):
        print("__iadd__被調用！！")
        self.data.extend(rhs.data)
        return self



    def __neg__(self):
        '''此方法用来制定 - self 返回的规则'''
        # L = [-x for x in self.data]  #數據大時不方便使用
        L = (-x for x in self.data)   # 生成器表達是不生成列表
        return MyList(L)


    def __contains__(self, e):
        '''此方法用来实现 in　/ not in 运算符的重载'''
        print("__contains__被调用")
        for x in self.data:
            if x == e:
                return True
        return False


    
    # def __getitem__(self, i):
    #     print("__getitem__被调用, i=", i)
    #     if type(i) is not int:
    #         raise TypeError
    #     return self.data[i]



    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        if type(i) is int:
            print("正在做索引操作")
        elif type(i) is slice:
            print("正在做切片操作")
            print("切片的起始值:", i.start)
            print("切片的终止值:", i.stop)
            print("切片的步长:", i.step)
        else:
            raise KeyError
        return self.data[i]


    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v =', v)
        self.data[i] = v  # 修改data绑定的列表
    


L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1,2,3,4,5,6])
L4 = L2 + L1
print(L4)  # MyList([4,5,6,1,2,3])
L5 = L1 * 2      #L1.__mul__(2)
print(L5)  # MyList([1,2,3,1,2,3])



L6 = 2 * L1  # 2.__mul__(L1)
print(L6)

L1+=L2      # 当没有__iadd__方法时，等同于调用L1 = L1 + L2
print(L1)

L7 = MyList([1, -2, 3, -4])
L8 = -L7
print(L8)


if -2 in L7:
    print('-2 在 L7 中')
else:
    print('-2 不在 L7中')


# 当MyList的类内重载了__contains__方法，则not in也同时可用
if -3 not in L7:
    print("-3 不在 L7中")
else:
    print('-3 在 L8中')



L9 = MyList([1, -2, 3, -4, 7, 8])  #__init__被调用
v = L9[-1]                        #__getitem__被调
print(v)                          #8

L9[1] = 2                         # 等同于调用 L1.__setitem__(1, 2)           __setitem__被调用, i= 1 v = 2
print(L9)                         #MyList([1, 2, 3, -4, 7, 8])

# 以下操作会出错
# print(L1[100000000000])
# print(L9['hello'])



L10 = MyList([1, -2, 3, -4, 5, -6])

print(L10[::2])  # 等同于调用L1[slice(None, None, 2)]

# __init__被调用
# __getitem__被调用, i= slice(None, None, 2)
# 正在做切片操作
# 切片的起始值: None
# 切片的终止值: None
# 切片的步长: 2
# [1, 3, 5]



# ubuntu@ubuntu-VirtualBox:~/aid1805/class$ python3 05_mylist.py
# <__main__.MyList object at 0x7fa2d5f98e10>
# <__main__.MyList object at 0x7fa2d5f98e48>
# <__main__.MyList object at 0x7fa2d5f98e80>


# __init__被调用
# __init__被调用
# __add__被调用
# __init__被调用
# MyList([1, 2, 3, 4, 5, 6])
# __add__被调用
# __init__被调用
# MyList([4, 5, 6, 1, 2, 3])
# __mul__被调用
# __init__被调用
# MyList([1, 2, 3, 1, 2, 3])
# __rmul__被调用
# __init__被调用
# MyList([1, 2, 3, 1, 2, 3])
# __iadd__被調用！！
# MyList([1, 2, 3, 4, 5, 6])
# __init__被调用
# __init__被调用
# MyList([-1, 2, -3, 4])
# __contains__被调用
# -2 在 L7 中
# __contains__被调用
# -3 不在 L7中
