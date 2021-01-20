# 字符串(开始索引：结束索引：步长)
# 切片结果包括开始索引，但是不包括结束索引
# 倒序索引：-1，-2 从右往左， 结束索引为空的时候，就可以切到末尾字符
num_str = "0123456789"
# 截取2-5字符
print(num_str[2:6])
# 截取2-末尾字符
print(num_str[2:])
# 截取从开始到5的字符
print(num_str[:6])
# 截取完整的字符串
print(num_str[:])
# 从索引1开始，每隔一个取一个
print(num_str[1::2])
print(num_str[::2])
# 从2开始到倒数第二个字符
print(num_str[2:-1])
# 截取字符串末尾两个字符
print(num_str[-2:])
# 字符串的逆序
print(num_str[-1::-1])
print(num_str[::-1])




