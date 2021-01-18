name_list = ["张三", "李四", "王五", "王二麻子"]
num_list =[1, 2, 3, 4, 5, 66, 3, 5, 6, 2, 0]
# 排序使用sort方法
name_list.sort()
num_list.sort()
# 逆序排序
name_list.sort(reverse=True)
num_list.sort(reverse=True)

name_list.reverse()
num_list.reverse()

# 关键字使用不需要小括号
# 函数封装了独立的功能，可以直接调用
# 但是函数需要死记硬背
# 方法和函数类似，同样是封装了独立的功能
# 方法需要通过对象来调用，表示对这个对象要做的操作。所以方法名一般不用记忆


print(name_list)
print(num_list)
