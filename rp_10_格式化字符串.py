info_tuple = ("诸葛不亮", 19, 1.90)
# 格式化字符串后面的 “()” 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % ("诸葛亮", 18, 1.85))
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
info_char = ("%s 年龄是 %d 身高是 %.2f" % info_tuple)
print(info_char)
# 可以使用 list（）和 tuple（）两个函数来转换list 和 tuple变量
num_list = [1, 2, 3, 4, 5]
num_tuple = tuple(num_list)
print(type(num_tuple))
print(num_tuple.index(3))
