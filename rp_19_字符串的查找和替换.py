hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hallo"))

# 2. 判断是否以指定的字符串结束
print(hello_str.endswith("world"))

# 3. 查找指定字符串
print(hello_str.find("lo"))
# index如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1
print(hello_str.find("asd"))

# 4. 替换字符串
# replace方法执行完毕后，会返回一个新的字符串
# 注意：不会改变原有的字符串内容

print(hello_str.replace("wor", "猪哥哥"))
print(hello_str)