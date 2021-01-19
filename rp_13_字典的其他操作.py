xiaoming_dic = {"name": "小明",
                "age": 19,
                "gender": True}

# 1. 统计键值对数量 (len)
print(len(xiaoming_dic))

# 2. 合并字典 (update)
temp_dic = {"height": 1.75,
            "weight": 85,
            "age": 20}

# 注意: 如果被合并的字典中包含已经存在过的键值时,会覆盖原有的键值对
xiaoming_dic.update(temp_dic)
print("合并以后的键值对数量是：%d" % len(xiaoming_dic))

# 3. 清空字典 (clear)
# xiaoming_dic.clear()

print(xiaoming_dic)
