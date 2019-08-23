# class student:
# 	def set_info(self,name,age=0):
# 		'''此方法用來給學生添加姓名何年齡屬性'''
# 		self.name =name
# 		self.age=age
# 	def show_info(self):
# 		'''此處顯示學生訊息'''
# 		print(self.name,'今年',self.age,'歲')

# s1=student()
# s1.set_info('小張',20)
# s2=student()
# s2.set_info('小李',22)
# s1.show_info()
# s2.show_info()

# 小張 今年 20 歲
# 小李 今年 22 歲
################################################################################################
# class Car:
# 	def __init__(self,c,b,m):
# 		# print("__init__方法被調用")
# 		self.color= c    #顏色
# 		self.brand= b    #品牌
# 		self.modle= m    #型號

# 	def run(self,speed):
# 		print(self.color,'的',self.brand,self.modle,'正在以',speed,'公里/小時的時速前進！')

# 	def set_color(self,clr):
# 		'''修改車顏色'''
# 		self.color =clr
# a4=Car('紅色','BMW','850i')

# a4.run(234)
# a4.set_color('黑色')
# a4.run(288)

# # 紅色 的 BMW 850i 正在以 234 公里/小時的時速前進！
# a4.modle='M6'
# a4.run(280)

# 紅色 的 BMW 850i 正在以 234 公里/小時的時速前進！
# 黑色 的 BMW 850i 正在以 288 公里/小時的時速前進！
# 黑色 的 BMW M6 正在以 280 公里/小時的時速前進！


################################################################################################
# 練習: 修改之前的student類，
# 1)為該類添加初始化方法，時現在創建對象自動設置
# '姓名' ，'年齡' ，'成績' 屬性
# 2)添加set_score方法能為對象修改成績訊息
# 3)添加show_info方法打印薛生對象的訊息

class student:
	def __init__(self,name,age=0,score=0):
		'''此方法用來給學生添加姓名何年齡屬性'''
		self.name =name
		self.age=age
		self.score=score
	def show_info(self):
		'''此處顯示學生訊息'''
		print(self.name,'今年',self.age,'歲','成績是',self.score)

	def set_score(self,s):
		self.score=s

s1=student('小張',20)
s2=student('小李',22,100)
s1.show_info()
s2.show_info()
s1.set_score(98)
s1.show_info()

小張 今年 20 歲 成績是 0
小李 今年 22 歲 成績是 100
小張 今年 20 歲 成績是 98

