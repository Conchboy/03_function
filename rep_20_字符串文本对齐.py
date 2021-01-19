# 假设，一下内容是从网上抓取的
# 要求，顺序并居中对齐输出以下内容
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))

"""
for poem_str1 in poem:
    print("|%s|" % poem_str1.rjust(10, "　"))


for poem_str2 in poem:
        print("|%s|" % poem_str2.ljust(10, "　"))
"""

