n = int(input())

flag = True
c = n + 1

while flag:
    for i in range(1, n+1):
        if c % i != 0:
            flag = False
            break
    
    if flag:
        print(c)
        break
    else:
        c += 1
        flag = True