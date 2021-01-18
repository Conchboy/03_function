name_list = ["zhangsan", "lisi", "wangwu"]

# 使用del关键字（delete）删除列表元素

del name_list[1]

name = "小明"

del name
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
# del关键字本质上事用来将一个变量从内存中删除，释放内存，从而以后再也不能访问了
# print(name)

print(name_list)
