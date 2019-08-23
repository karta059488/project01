# 面向对象的综合示例
#   有两个人:
#     1.
#       姓名: 张三
#       年龄: 35
#     2.
#       姓名: 李四
#       年龄: 8
#     行为:
#       1. 教别人学东西 teach
#       2. 赚钱
#       3. 借钱
#   事情:
#      张三 教 李四 学 python
#      李四 教 张三 学 跳皮筋
#      张三 上班赚了 1000元钱
#      李四向张三借了 200元

class Human:
  '''人類'''
  def __init__(self,n,a):
    self.name =n
    self.age = a
    self.money = 0

  def teach(self,other,skill):
    print(self.name,'教',other.name,'學',skill)

  def works(self,money):
    self.money += money
    print(self.name,'工作賺了',money,'元')

  def borrow(self,other,money):
    if other.money > money :     #判對他有這多錢
      print(other.name,'借給',self.name,money,'元錢')
      other.money -= money
      self.money += money
    else:
      print(other.name,'不借給',self.name)   #它沒遮多錢可借

  def show_info(self):
    print(self.age,'歲的',self.name,'存有',self.money,'元')

zhang3 =Human('張三',35)
li4 = Human('李四',8)
zhang3.teach(li4,'python')
li4.teach(zhang3,'跳皮筋')
zhang3.works(1000)
li4.borrow(zhang3,200)
zhang3.show_info()
li4.show_info()



# 張三 教 李四 學 python
# 李四 教 張三 學 跳皮筋
# 張三 工作賺了 1000 元
# 張三 借給 李四 200 元錢
# 35 歲的 張三 存有 800 元
# 8 歲的 李四 存有 200 元
