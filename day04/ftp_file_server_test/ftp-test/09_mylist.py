class Mylist:
	def __init__(self,iterator=[]):
		self.data = [x for x in iterator]

	def __repr__(self):
		return "Mylist(%r)" % self.data

	def __abs__(self):
        # return MyList([abs(x) for x in self.data])
        # 上一句语句可以用如下生成表达式代替已防止过多占内存
		return Mylist((abs(x) for x in self.data))

	def __len__(self):
		# return self.data.__len__()
		return len(self.data)

myl = Mylist([1,-2,3,-4])
print(myl)
print(abs(myl))
print("原來得列表是：",myl)

myl2 = Mylist(range(10))
print("myl2的長度是：",len(myl2))
print("myl的長度是：",len(myl))




# Mylist([1, -2, 3, -4])
# Mylist([1, 2, 3, 4])
# 原來得列表是： Mylist([1, -2, 3, -4])
# myl2的長度是： 10
# myl的長度是： 4
