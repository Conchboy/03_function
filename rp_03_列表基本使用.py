name_list = ["zhangsan", "lisi", "wangwu"]
# 1. 取值和取索引
print([name_list[0]])
# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果所确定的数据不在列表中，那么会报错
print(name_list.index("lisi"))

# 2. 修改
name_list[1] = "李四"
name_list[2] = "王小二"


# 3. 增加
name_list.append("诸葛亮")
name_list.extend("你是谁")
name_list.insert(2, "小猪头")

temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

# 4. 删除
name_list.pop()
# pop方法可以指定要删除的元素的索引
name_list.pop(3)
name_list.remove("诸葛亮")
# clear方法可以清空列表
# name_list.clear()
print(name_list.index("猪二哥"))

print(name_list)
