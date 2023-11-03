n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split(',')))
    matrix.append(row)

diag = True

for i in range(n):
    for j in range(n):
        if i != j and matrix[i][j] != 0:
            diag = False
            break
    if not diag:
        break

if diag:
    scalar = True
    init_elem = matrix[0][0]
    for i in range(n):
        if matrix[i][i] != init_elem:
            scalar = False
            break
        
    if scalar:
        identity = True
        if init_elem != 1:
            identity = False

if identity:
    print('Identity Matrix')
elif scalar:
    print('Scalar Matrix')
elif diag:
    print('Diagonal Matrix')
else:
    print('Not Diagonal')