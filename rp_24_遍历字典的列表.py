# 在迭代遍历嵌套的数据类型时，例如一个列表包含了多个字典
# 需求： 要判断某一个字典中是否存在指定的值
# 如果存在， 提示并退出循环
# 如果不存在，在循环整体结束后，希望得到一个统一的提示。

students = [
    {"name": "安徒生"},
    {"name": "美羊羊"},
    {"name": "土八路"}
]

# 在学员列表中搜索制定的姓名
find_name ="ss"
for student_dic in students:
    print(student_dic)
    if student_dic["name"] == find_name:
        print("找到了 %s" % find_name)
        # 如果已经找到，应该直接退出循环，而不在遍历后续的元素
        break
    # else:
    #     print("抱歉没有找到： %s" % find_name)
else:
    # 如果希望在搜索列表时，所有的字典被检查后， 都没有发现要搜索的目标
    # 还希望得到一个统一的提示
    print("抱歉没有找到 % s" % find_name)


print("循环结束")