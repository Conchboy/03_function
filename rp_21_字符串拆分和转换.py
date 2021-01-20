# 假设，一下内容是从网上抓取的
# 要求，分隔字符串中的各元素，并以空格作为分隔符合并列表中的元素到一个新的字符串中
# 使用split方法（默认以空格作为分隔符）来分隔字符串，产生一个新的列表；
# 使用join方法，以string.join( 待合并的字符串列表）将字符串合并并以string分隔

poem_str = "\t\n登鹳雀楼 王之涣\t  \n白日依山尽 黄河入海流 欲穷千里目\t  更上一层楼"
print(poem_str)

poem_list = poem_str.split()

print(poem_list)

result_str = "\n".join(poem_list)

print(result_str.center(10))

for result in result_str.split():
    print("|%s|" % result.center(15), "　")
