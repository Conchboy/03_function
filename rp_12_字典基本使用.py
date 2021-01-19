xiaoming_dict = {"name": " 小明"}
# 1.取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的课不存在，程序会报错！
# print(xiaoming_dict["name1234"])

# 2.增加/修改
# 如果key不存在，会增加新的键值对
xiaoming_dict["age"] = 18
# 如果Key存在，那么会修改已经存在的键值对
xiaoming_dict["age"] = 20
xiaoming_dict["name"] = "小小明"

# 3.删除

print(xiaoming_dict)
