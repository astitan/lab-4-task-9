#9. Формируется матрица F следующим образом: если в В количество строк, состоящих из одних нулей в четных столбцах в области
#2 больше, чем сумма положительных элементов в четных строках в области 4, то поменять в С симметрично области 1 и 2 местами,
#иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*F)*А– (K * AT).
#Выводятся по мере формирования А, F и все матричные операции последовательно.
import random
import time
print("Еnter an even number that will be in the interval from 6 to 100\nEnter size of matrix: ")
N = int(input())
while (N % 2 != 0) or (N < 6):
    print("Еnter an even number that will be in the interval from 6 to 100\nEnter size of matrix: ")
    N = int(input())
print("Enter ratio: ")
K = int(input())
start = time.time()
matrix_A = []
for i in range(N):                                      #creating matrix A
    submatrix_A = []
    for j in range(N):
        submatrix_A.append(random.randint(-1,1))
    matrix_A.append(submatrix_A)
time_next = time.time()
print("Matrix A: ", time_next-start)
for i in matrix_A:                                       #print matrix A
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
matrix_B = []
for i in range(int(N/2)):                               #selection of the matrix B area
    submatrix_B = []
    for j in range(int(N/2)):
         submatrix_B.append(matrix_A[i][j])
    matrix_B.append(submatrix_B)
time_prev = time_next
time_next = time.time()
print("matrix B", time_next-time_prev)
for i in matrix_B:                                      #print matrix B
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
count_zero = 0                                          #zero row counter
for i in range(int(N/2)):
    sum1 = 0                                            #counter of even columns in a row
    sum2 = 0                                            #counter of even columns with zero row
    for j in range(int(N/2)):                           #the number of rows consisting of only zeros in even columns in area 2
        if (((i < j) and (i < N/2-j-1)) and (j % 2 != 0) and (matrix_B[i][j] == 0)):
            sum1 += 1
        if (((i < j) and (i < N/2-j-1)) and (j % 2 != 0)):
            sum2 += 1
    if i >= N/2 - N/4 - 1:
        break
    if sum1 == sum2:
        count_zero += 1
count_sum = 0                                        #sum of positive elements
for i in range(int(N/2)):                            #the sum of positive elements in even rows in area 4
    for j in range(int(N/2)):
        if ((i > j) and (i > N/2-j-1)) and (i % 2 != 0) and (matrix_B[i][j] > 0):
            count_sum += matrix_B[i][j]
matrix_F = []
for i in range(N):                                              #creating matrix F
    submatrix_F = []
    for j in range(N):
         submatrix_F.append(matrix_A[i][j])
    matrix_F.append(submatrix_F)
time_prev = time_next
time_next = time.time()
print("matrix F", time_next-time_prev)
for i in matrix_F:                                          #print matrix F
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
matrix_C = []
for i in range(0,int(N/2),1):                           #selection of the matrix C area
    submatrix_C = []
    for j in range(int(N/2),N,1):
         submatrix_C.append(matrix_A[i][j])
    matrix_C.append(submatrix_C)
time_prev = time_next
time_next = time.time()
print("matrix C", time_next-time_prev)
for i in matrix_C:                                          #print matrix C
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
matrix_E = []
for i in range(int(N/2),N,1):                               #selection of the matrix E area
    submatrix_E = []
    for j in range(int(N/2),N,1):
         submatrix_E.append(matrix_A[i][j])
    matrix_E.append(submatrix_E)
time_prev = time_next
time_next = time.time()
print("matrix E", time_next-time_prev)
for i in matrix_E:                                          #print matrix E
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
if count_zero > count_sum:
    print("\nthe first condition was fulfilled")
    for i in range(int(N/2)):                                      #the first condition of the permutation is fulfilled
        temp = 0
        for j in range(int(N/2)):
            if (i < N/2-j-1) and (i < j):
                temp = matrix_C[i][j]
                matrix_C[i][j] = matrix_C[j][i]
                matrix_C[j][i] = temp
else:
    print("\nthe second condition was fulfilled")
    for i in range(int(N/2)):                                              #the second condition of the permutation is fulfilled
        temp = 0
        for j in range(int(N/2)):
            temp = matrix_C[i][j]
            matrix_C[i][j] = matrix_E[i][j]
            matrix_E[i][j] = temp
time_prev = time_next
time_next = time.time()
print("new matrix C", time_next-time_prev)
for i in matrix_C:                                                      #print new matrix C
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
print("new matrix E")
for i in matrix_E:                                                      #print new matrix E
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
for i in range(int(N/2)):                                   #fill the matrix F with a new submatrix C
    for j in range(int(N/2),N,1):
        matrix_F[i][j] = matrix_C[i][j-int(N/2)]
for i in range(int(N/2),N,1):                               #fill the matrix F with a new submatrix E
    for j in range(int(N/2),N,1):
        matrix_F[i][j] = matrix_E[i-int(N/2)][j-int(N/2)]
time_prev = time_next
time_next = time.time()
print("new matrix F", time_next-time_prev)
for i in matrix_F:                                              #print new matrix F
    for j in i:
        print("{:4d}".format(j), end = "")
    print()
for i in range(N):                                                  #multiplication of matrix F on digit K
    for j in range(N):
        matrix_F[i][j] = matrix_F[i][j] * K
time_prev = time_next
time_next = time.time()
print("new matrix F * K", time_next-time_prev)
for i in matrix_F:                                                  #print new matrix F * K
    for j in i:
        print("{:6d}".format(j), end = "")
    print()
matrix_KFA = []                                                         #creating matrix (K*F)*A
for i in range(N):
    submatrix_KFA = []
    for j in range(N):
         submatrix_KFA.append(matrix_F[i][j])
    matrix_KFA.append(submatrix_KFA)
for i in range(N):                                                      # K*A*F
    for j in range(N):
        s = 0
        for m in range(N):
            s = s + matrix_F[i][m] * matrix_A[m][j]
        matrix_KFA[i][j] = s
time_prev = time_next
time_next = time.time()
print("new matrix F * K * A", time_next-time_prev)
for i in matrix_KFA:                                                #print new matrix (K*F)*A
    for j in i:
        print("{:6d}".format(j), end = "")
    print()
matrix_AT = []
for i in range(N):                                              #creating matrix AT
    submatrix_AT = []
    for j in range(N):
         submatrix_AT.append(matrix_A[i][j])
    matrix_AT.append(submatrix_AT)
for i in range(N):                                                  #transposition of matrix A
    temp = 0
    for j in range(i,N,1):
        temp = matrix_A[i][j]
        matrix_A[i][j] = matrix_A[j][i]
        matrix_A[j][i] = temp
time_prev = time_next
time_next = time.time()
print("transposition matrix A", time_next-time_prev)
for i in matrix_A:                                                  #print transposition matrix A
    for j in i:
        print("{:6d}".format(j), end = "")
    print()
for i in range(N):                                          #multiplication of transposition matrix A on digit K
    for j in range(N):
        matrix_AT[i][j] = matrix_AT[i][j] * K
time_prev = time_next
time_next = time.time()
print("transposition matrix A * K", time_next-time_prev)
for i in matrix_AT:                                              # print transposition matrix A * K
    for j in i:
        print("{:6d}".format(j), end="")
    print()
result_matrix = []                                              #creating result matrix
for i in range(N):
    submatrix_result_matrix = []
    for j in range(N):
         submatrix_result_matrix.append(matrix_KFA[i][j])
    result_matrix.append(submatrix_result_matrix)
for i in range(N):
    for j in range(N):
        result_matrix[i][j] = matrix_KFA[i][j] - matrix_AT[i][j]
time_prev = time_next
time_next = time.time()
print("result matrix", time_next-time_prev)
for i in result_matrix:                                             # print result matrix
    for j in i:
        print("{:6d}".format(j), end="")
    print()
finish = time.time()
result = finish - start
print("Program time: " + str(result) + " seconds.")
