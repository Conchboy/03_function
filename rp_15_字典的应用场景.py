# 实际开发常用的应用场景：
# 使用字典存储描述一个物体（对象）的相关信息：比如一个学生的相关信息
# 使用列表来安放上述生成的不同物体（对象）的字典集合
card_list= [
    {"name": "张三",
     "qq": "12345",
     "phone": "10086"},

    {"name": "李四",
     "qq": "0873214",
     "phone": "96888"}
]

for card_info in card_list:
    print(card_info)
