# 练习:
#   实现有序集合 OrderSet 类 能实现两个集合的交集 &, 并集 |, 补集 -, 对称补集 ^, ==, != , in / not in集合操作
#   (要求集合内用 list 存储数据)
#   s1 = OrderSet([1, 2, 3, 4])
#   s2 = OrderSet([3, 4, 5])
#   print(s1 & s2)  # OrderSet([3, 4])
#   print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
#   print(s1 ^ s2)  # OrderSet([1, 2, 5])
#   if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
#       print("不相等")
#   if s2 == OrderSet(3,4,5):
#      print("s2 和 OrderSet(3,4,5)相等")
#   if 2 in s1:
#       print("2 in s1")


class OrderSet:
    def __init__(self, it=None):
        if it is None:
            self.data = []
        elif it:
            self.data = [x for x in it]

    def __repr__(self):
        return "OrderSet(%r)" % self.data

    def __and__(self, rhs):    #交集
        return OrderSet(
            (x for x in self.data if x in rhs.data)    #何右邊的資料相同
        )

    def __or__(self, rhs):　　　　　#並集
        return OrderSet(
            self.data + [x for x in rhs.data
                         if x not in self.data]　　　　　　#左邊的資料加上　　　右邊資料不在左邊範為內　　
        )

    def __sub__(self, rhs):   #補集
        return OrderSet(
            (x for x in self.data if x not in rhs.data)   #左邊資料扣掉在右邊範為內剩下的
        )

    def __xor__(self, rhs):　　　#對稱補集
        return (self - rhs) | (rhs - self)

    def __eq__(self, rhs):
        return self.data == rhs.data

    def __ne__(self, rhs):
        return self.data != rhs.data

    def __contains__(self, ele):
        return ele in self.data


s0 = OrderSet()
s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  # OrderSet([3,4])
print(s1 | s2)  # OrderSet([1,2,3,4,5])
print(s1 - s2)  # OrderSet([1,2])
print(s1 ^ s2)  # OrderSet([1,2,5])
if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4]):
    print("不相等")
# 思考是否可以实现以下操作?
if 2 in s1:
    print("2 在 s1 内")

if 100 not in s1:
    print("100 不在 s1 内")


# OrderSet([3, 4])
# OrderSet([1, 2, 3, 4, 5])
# OrderSet([1, 2])
# OrderSet([1, 2, 5])
# 不相等
# 2 在 s1 内
# 100 不在 s1 内
