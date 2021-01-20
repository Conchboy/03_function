for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如何在for循环中使用了break，那么后面的else就不会被执行
    print("会执行吗？")