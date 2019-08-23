# 此示例示意继承和派生
class Human:
	'''此类用来描述人类的共性行为'''
	def say (self,that):
		print('說：',that)
	def walk(self,distance):
		print("走:",distance,'公里')


class student(Human):
	def study(self,subject):
		print("正在學習",subject)

class Teacher(Human):
	def teach(self,subject):
		print("正在教",subject)


h1 = Human()
h1.say('今天天氣真熱')
h1.walk(5)

print('-------以下是学生对象的行为-----------')
s1 = student()
s1.say("學習有點累")
s1.walk(3)
s1.study("python")

t1 =Teacher()
t1.say("明天就星期六了")
t1.walk(9)
t1.teach("面向對象")




# 說： 今天天氣真熱
# 走: 5 公里
# -------以下是学生对象的行为-----------
# 說： 學習有點累
# 走: 3 公里
# 正在學習 python
# 說： 明天就星期六了
# 走: 9 公里
# 正在教 面向對象
