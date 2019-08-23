# 練習2:
#    寫一個類,Fibonacci 實現迭代器協定,此類的物件可以作為可反覆運可迭代對象生成相應的斐波那契數
#      1 1 2 3 5 8 ....

#     class Fibonacci:
#         def __init__(self, n):
#            ...

#     實現如下操作:
#     for x in Fibonacci(10):
#         print(x)
#     L = [ x for x in Fibonacci(30)]
#     print(sum(Fibonacci(25)))
#       (需要實現迭代器協定)




# 提示: 可以用一個類來實現,也可以用兩個類實現
#     class Fibonacci:
#         def __init__(self, n):
#            ...

#         def __iter__(self):
#             ....

#         def __next__(self):
#             ....

class Fibonacci:
  def __init__(self, n):
    self.__count = n

  def __iter__(self):
    return FiboIterator(self.__count)

class FiboIterator:
  def __init__(self,n):
    self.__count = n
    self.cur_count = 0
    self.a =0    #用來保存前第二個數
    self.b =1    #用來保存前一個數

  def __next__(self):
    if self.cur_count >= self.__count:
      raise StopIteration
    self.cur_count += 1
    self.a, self.b = self.b, +self.a + self.b
    return self.a



# 方法2
# class Fibonacci:
#     def __init__(self, n):
#         self.__count = n

#     def __iter__(self):
#         self.cur_count = 0
#         self.a = 0  # 用来保存前第二个数
#         self.b = 1  # 用来保存前一个数
#         return self


#     def __next__(self):
#         if self.cur_count >= self.__count:
#             raise StopIteration
#         self.cur_count += 1  # 生成数加1
#         self.a, self.b = self.b, self.a + self.b
#         return self.a



for x in Fibonacci(10):
  print(x)
   
L = [ x for x in Fibonacci(30)]
print(L)
print(sum(Fibonacci(10)))
      # (需要實現迭代器協定)


# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
# 143
