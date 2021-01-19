hello_str = "hello hello"

#  1. 统计字符串长度
print(len(hello_str))

# 2. 统计某一字符串出现的次数
print(hello_str.count("hell"))
# 子字符串如果不在母字符串中，那么输出0
print(hello_str.count("abc"))

# 3. 某一子字符串出现的位置
print(hello_str.index(" "))
# 子字符串没有找到的话，程序会报错
print(hello_str.index("ls"))


