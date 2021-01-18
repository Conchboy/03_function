def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    for i in range(10):
        print_line(char, times)


name = "河马程序员"

print_lines("天空 ", 10)
