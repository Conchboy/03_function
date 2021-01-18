name_list = ["zhangsan", "lisi", "wangwu"]

# len函数可以统计列表中元素的总和
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

# count方法可以统计列表中某一个数据出现的次数
for i in range(5):
    name_list.append("lisi")

count = name_list.count("lisi")
print("lisi出现了 %d 次" % count)

name_list.remove("wangwu")

print(name_list)

