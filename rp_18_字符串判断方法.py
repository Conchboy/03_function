# 1. 判断空白字符
space_str = " \t\n\r" # 也可以判断回车，换行等空白字符

print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
num_str = "三"

print(num_str)
# 都不能判断小数， isdigital()可以判断unicode，比如平方的上标， isnumeric()可以判断中文

print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())


