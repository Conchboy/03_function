xiaoming_dict = {"name": "小明",
                 "qq": "12345666",
                 "phone": "1008666"}

# 迭代遍历字典 (打印K和dict[k]的值）
# 变量k是每一次循环中，获得到的键值对的key


for k in xiaoming_dict:
    print("%-6s ： %s" % (k, xiaoming_dict[k]))
