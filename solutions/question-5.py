A = int(input())

for i in range(A + 1):
    flag = True
    for j in range(i + 1):
        if ((i * j) == A):
            print(j, i, sep=",")
            flag = False
            break
        
    if not flag:
        break