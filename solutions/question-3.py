# Method-1
n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split(',')))
    matrix.append(row)

diag = True
scalar = identity = False

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

"""-----------------------------------------------------------------------"""
# Method-2
n=int(input())
M=[]
for i in range(n):
	row=list(map(int,input().split(',')))
	M.append(row)

is_diagonal=True
is_scalar = True
is_identity = True
for i in range(n):
	for j in range(n):
			if i != j and M[i][j] != 0:
					is_diagonal = False
			if i != j and M[i][j] != M[0][0]:
					is_scalar = False
			if i == j and M[i][j] != 1:
					is_identity = False
if is_identity:
	print('identity')
elif is_scalar:
	print('scalar')
elif is_diagonal:
	print('diagonal')
else:
	print('non-diagonal')
       
"""-----------------------------------------------------------------------"""
# Method - 3       
def check_matrix_type(matrix):
  n = len(matrix)
  m = len(matrix[0])

  is_diagonal = True
  is_scalar = True
  is_identity = True

  # Check for different matrix types
  for i in range(n):
      for j in range(m):
          if i == j and matrix[i][j] != matrix[0][0]:
              is_scalar = False

          if i == j and matrix[i][j] != 1:
              is_identity = False
          elif i != j and matrix[i][j] != 0:
              is_identity = False
  if is_identity:
    return "identity"
  elif is_diagonal and not is_scalar:
      return "diagonal"
  elif is_diagonal and is_scalar:
      return "scalar"
  else:
      return "non-diagonal"

n = int(input("Enter the number of rows: "))
matrix = []
for i in range(n):
  row = list(map(int, input().split(',')))
  matrix.append(row)

matrix_type = check_matrix_type(matrix)
print(f"The type of the matrix is: {matrix_type}")

"""-----------------------------------------------------------------------"""
# Method - 4
n = int(input())
mat = []
for i in range(n) :
    st = input().split(',')
    st = list(map(int, st))
    mat.append(st)
first = mat[0][0]
scalar = True
identity = non = False
for i in range(n) :
    for j in range(n) :
        if ((i != j) and (mat[i][j] != 0)) :
            non = True
        if (i == j) and (mat[i][j] != first):
            scalar = False
if scalar and first == 1 :
    identity = True
if non :
    print("Non-Diagonal")
elif identity :
    print("Identity")
elif scalar :
    print("Scalar")
else :
    print("Diagonal")