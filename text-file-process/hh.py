with open('log_files/201811123009.log', encoding='utf8')as f:
    n = 0
    for line in f:
        alist = list(map(str, line.split(' ')))
        if alist[1] == "学号：201811123009,":
            n += 1
    print(n)