c = 9
for i in range(9, -2, -1):
    if i%3==0 and i!=9:
        c += 1
    if i <= 0:
        space = " " * 8
        leaf = "█" * 3
    else:    
        space = " " * (c)
        n = (19-c*2)//2
        if i != 9:
            leaf = "/" * n + "|" + "\\" * n
        else:
            leaf = "*"
    c -= 1
    print(space + leaf)
