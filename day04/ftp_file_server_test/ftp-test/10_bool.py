class Mylist:
	def __init__(self,iterator=[]):
		self.data = [x for x in iterator]

	def __repr__(self):
		return "Mylist(%r)" % self.data

	def __abs__(self):
        # return MyList([abs(x) for x in self.data])
        # 上一句语句可以用如下生成表达式代替已防止过多占内存
		return Mylist((abs(x) for x in self.data))

	# def __len__(self):
	# 	# return self.data.__len__()
	# 	print("__len__方法被調用！")
	# 	return len(self.data)


	def __bool__(self):
		print("__bool__方法被調用！")
		return False

myl = Mylist([1,-2,3,-4])
print(bool(myl))
if myl:
	print("myl是真直")
else:
	print("myl是假植")