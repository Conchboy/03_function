xiaoming_dict = {"name": "小明",
                 "qq": "12345666",
                 "phone": "1008666"}

# 迭代遍历字典 (打印K和dict[k]的值）
# 变量k是每一次循环中，获得到的键值对的key


for k in xiaoming_dict: # 这里的变量k是获得的键值
    print("%-6s ： %s" % (k, xiaoming_dict[k]))
# 实际开发常用的应用场景：
# 使用字典存储描述一个物体（对象）的相关信息：比如一个学生的相关信息
# 使用列表来安放上述生成的不同物体（对象）的字典集合
