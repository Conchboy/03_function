students = [
    {"name": "安徒生"},
    {"name": "美羊羊"},
    {"name": "土八路"}
]

# 在学员列表中搜索制定的姓名
find_name ="安徒生"
for student_dic in students:
    print(student_dic)
    if student_dic["name"] == find_name:
        print("找到了 %s" % find_name)
        # 如果已经找到，应该直接退出循环，而不在遍历后续的元素
        break
else:
    print("抱歉没有找到 % s" % find_name)


print("循环结束")