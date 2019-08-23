# 練習
#   1. 用類來描述一個學生的資訊(可以修改之前的寫的Student類)
#     class Student:
#           # 此處自己實現
    
#     要求該類的物件用於存儲學生資訊:
#          姓名,年齡,成績
#     將這些物件存於清單中.可以任意添加和刪除學生資訊
#        1. 列印出學生的個數
#        2. 列印出所有學生的平均成績
#     (建議用類變數存儲學生的個數,也可以把清單當作類變數)

class Student:
    count = 0  # 此类变量用来记录学生的个数

    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s
        Student.count += 1  # 让对象个数加1
    def __del__(self):
        Student.count -= 1  # 对象销毁时count减1

    def get_score(self):
        return self.score

    @classmethod
    def getTotalCount(cls):
        '''此方法用来得到学生对象的个数'''
        return cls.count


def test():
    L = []  # 1班的学生
    L.append(Student('小张', 20, 100))
    L.append(Student('小王', 18, 97))
    L.append(Student('小李', 19, 98))
    print('此时学生对象的个数是:',Student.getTotalCount())

    L2 = []  # 2班学生
    L2.append(Student('小赵', 18, 55))
    print(Student.getTotalCount())  # 4
    # 删除L中的一个学生
    L.pop(1)   #刪掉小王
    print("此时学生个数为:", Student.getTotalCount())

    all_student = L + L2
    scores = 0  # 用此变量来记录所有学生的成绩总和
    for s in all_student:
        # scores += s.score  # 累加所有学生的成绩
        scores += s.get_score()    #用方法操作實力變量

    print("平均成绩是:", scores/len(all_student))


if __name__ == '__main__':
    test()



# 此时学生对象的个数是: 3
# 4
# 此时学生个数为: 3
# 平均成绩是: 84.33333333333333

