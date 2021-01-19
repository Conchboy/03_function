# 假设，一下内容是从网上抓取的
# 要求，顺序并居中对齐输出以下内容
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "\n白日依山尽",
        "黄河入海流",
        "欲穷千里目\t",
        "更上一层楼"]

for poem_str in poem:
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中
    print("|%s|" % poem_str.strip().center(15, "　"))


"""
for poem_str1 in poem:
    print("|%s|" % poem_str1.rjust(10, "　"))


for poem_str2 in poem:
        print("|%s|" % poem_str2.ljust(10, "　"))
"""

