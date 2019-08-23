# 已知list 列表類中沒有insert_head方法,
#     寫一個自訂的類MyList,繼承自list類,在MyList類內添加

#     class MyList(list):
#       def insert_head(self, value):
#           '''以下自己實現,將Value插入到列表的開始處'''

#     如:
#       L = MyList(range(1,5))
#       print(L)  # [1,2,3,4]
#       L.insert_head(0)
#       print(L)  # [0,1,2,3,4]
#       L.append(5)
#       print(L)  # [0,1,2,3,4,5]

class Mylist(list):
  def insert_head(self,value):
      '''以下自己實現,將Value插入到列表的開始處'''
      self.insert(0,value)

L = Mylist(range(1,5))
print(L)        # [1,2,3,4]
L.insert_head(0)
print(L)  # [0,1,2,3,4]
L.append(5)
print(L)  # [0,1,2,3,4,5]