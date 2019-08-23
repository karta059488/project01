# 2. 寫一個類Bicycle(自行車)類,有run方法,調用時顯示騎行里程km
#   class Bicycle:
#       def run(self, km):
#           print("自行車騎行了", km, "公里")

#   再寫一個類EBicycle(電動自行車)類,在Bicycle類的基礎上添加電池電量volume屬性,有兩個方法:
#      1. file_charge(self, vol) 用來充電,vol為電量
#      2. run(km) 方法每騎行10km消耗電量1度, 同時顯示當前電量,當電量耗盡時,則調用Bicycle的run方法騎行
#     class EBicycle(Bicycle):
#          ...
#   b = Bicycle()
#   b.run(10)  # 自行車騎行了 10 公里
#   e = EBicycle(5)
#   e.run(10)  # 電動騎行了 10 公里
#   e.run(100) # 電動騎行了 40 公里, 自行車騎行了 60 公里
#   b.fill_charge(10)
#   b.run(100)


class Bicycle:
  def run(self, km):
    print("自行車騎行了", km, "公里")


class EBicycle(Bicycle):
  def __init__(self,vol):
    self.vol = vol  #用來記住電量

  def run (self,km):
    e_km =min(self.vol *10 ,km)  #電動的總數何km求最小
                 
    if e_km > 0:
      print("電動騎行了",e_km,"公里",end=';')
      self.vol -= e_km / 10
    km -= e_km
    if km > 0:
      super().run(km)


                 #以下是有問題的
    # if e_km <= km:
    #   print("電動騎行了",e_km,"公里")
    #   self.vol -= e_km / 10
    # else:
    #   print("電動騎行了",e_km,"公里",end=';')  #電力剩餘可騎行的距離
    #   self.vol -= e_km / 10
    #   super().run(km-e_km)
    print("本次剩餘電量",self.vol)

  def fill_charge(self,volume):    #執行充電
    self.vol += volume

b = Bicycle()
b.run(10)  # 自行車騎行了 10 公里
e = EBicycle(5)   #給它五度電
e.run(10)  # 電動騎行了 10 公里
e.run(100) # 電動騎行了 40 公里, 自行車騎行了 60 公里
e.fill_charge(10)
b.run(100)
e.run(55)


# 自行車騎行了 10 公里
# 電動騎行了 10 公里;本次剩餘電量 4.0
# 電動騎行了 40.0 公里;自行車騎行了 60.0 公里
# 本次剩餘電量 0.0
# 自行車騎行了 100 公里
# 電動騎行了 55 公里;本次剩餘電量 4.5
