import math
import matplotlib.pyplot as plt
import time

#########################################################################
# DZIALANIA NA MACIERZACH ###############################################
#########################################################################

def lu_factorization(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    
    for i in range(n):
        L[i][i] = 1.0
        
    for i in range(n):
        for j in range(i, n):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1
            
        for j in range(i+1, n):
            s2 = sum(U[k][i] * L[j][k] for k in range(i))
            L[j][i] = (A[j][i] - s2) / U[i][i]
    
    return L, U

def forward_subD(D, b):
    n = len(D)
    x = []
    for i in range(n):
        x.append(b[i] / D[i][i])
    return x

def backword_sub(U, b):
    n = len(U)
    x = [0] * n
    x[n-1] = b[n-1] / U[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += U[i][j] * x[j]
        x[i] = (b[i] - sum) / U[i][i]
    return x

def forward_sub(L, b):
    n = len(L)
    x = [0] * n
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= L[i][j] * x[j]
        x[i] /= L[i][i]
    return x

def norm(r):
    sum_of_squares = 0
    try:
        for i in range(len(r)):
            sum_of_squares += r[i]**2
    except OverflowError as e:
        print("norma błedu resydualnego = inf")
        return -1
    return math.sqrt(sum_of_squares)

def zeros(N):
    tab = []*N
    for i in range(N):
        tab.append([0]*N)
    return tab

def ones(N):
    tab = []
    for i in range(N):
        tab.append(1)
    return tab

def zadA(matrix,N):
    a1 = 5 + 6
    a2 = -1 
    a3 = -1
    for i in range(N):
        matrix[i][i] = a1
        if i+1 < N:
            matrix[i][i+1] = a2
        if i+2 < N:
            matrix[i][i+2] = a3  
        if i-1 >= 0:
            matrix[i][i-1] = a2
        if i-2 >= 0:
            matrix[i][i-2] = a3

def zadC(matrix,N):
    a1 = 3
    a2 = -1 
    a3 = -1
    for i in range(N):
        matrix[i][i] = a1
        if i+1 < N:
            matrix[i][i+1] = a2
        if i+2 < N:
            matrix[i][i+2] = a3  
        if i-1 >= 0:
            matrix[i][i-1] = a2
        if i-2 >= 0:
            matrix[i][i-2] = a3

def printMat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def diag(matrix, N):
    mat = zeros(N)
    for i in range(N):
        mat[i][i]= matrix[i][i]
    return mat

def tril(matrix, N):
    mat = zeros(N)
    for i in range(N):
        for j in range(0,i):
            mat[i][j]= matrix[i][j]
    return mat

def triu(matrix, N):
    mat = zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            mat[i][j]= matrix[i][j]
    return mat

def mulMatrixs(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        mat = []
        for j in range(len(matrix2[0])):
            sum = 0
            for z in range(len(matrix1[0])):
                sum += matrix1[i][z]*matrix2[z][j]
            mat.append(sum)
        matrix.append(mat)
    if len(matrix) == 1:
        return matrix[0]    
    return matrix

def mulMatrixAndVector(matrix1, vec):
    matrix = []
    for i in range(len(matrix1)):
        sum = 0
        for j in range(len(vec)):
            sum += matrix1[i][j]*vec[j]
        matrix.append(sum)
    return matrix

def mulMatrix(matrix1, I):
    matrix = []
    for i in range(len(matrix1)):
        mat = []
        for j in range(len(matrix1[0])):
            mat.append(matrix1[i][j]*I)
        matrix.append(mat)
    return matrix

def addM(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        mat = []
        for j in range(len(matrix1[0])):
            mat.append(matrix1[i][j]+matrix2[i][j])
        matrix.append(mat)
    return matrix

def subV(vec1, vec2):
    vec = []
    for i in range(len(vec1)):
        vec.append(vec1[i]-vec2[i])
    return vec

def addV(vec1, vec2):
    vec = []
    for i in range(len(vec1)):
        vec.append(vec1[i]+vec2[i])
    return vec

#########################################################################
# METODY ################################################################
#########################################################################

def Jacobi(matrix, N, b, o):
    if o == 1:
        print("\nMetoda Jacobiego")
    endWhile = 10**-9
    D = diag(matrix, N)
    L = tril(matrix, N)
    U = triu(matrix, N)
    mD = mulMatrix(D, -1)
    LU = addM(L,U)
    r2 = forward_subD(D,b)
    r = ones(N)
    res = 1
    norm_r = 1
    iteration = 0
    start_time = time.process_time()
    while norm_r > endWhile:
        iteration += 1
        LUr = mulMatrixAndVector(LU,r)
        r1 = forward_sub(mD,LUr)
        r = addV(r1,r2)
        res = mulMatrixAndVector(matrix, r)
        res = subV(res, b)
        norm_r = norm(res)
        if norm_r == -1:
            break
    end_time = time.process_time()
    timee = end_time - start_time
    if o == 1:
        print("Liczba iteracji dla metody Jacobiego", end=' ')
    if o == 1:
        print(iteration)
    if o == 1:
        print("Czas wykonywania: ", end_time - start_time)
    if norm_r != -1:
        if o == 1:
            print("Norma błedu resydualnego: ", norm_r)
    return timee

def JacobiD(matrix, N, b, o):
    if o == 1:
        print("\nMetoda Jacobiego z forward_sub dla macierzy diagonalnej")
    endWhile = 10**-9
    D = diag(matrix, N)
    L = tril(matrix, N)
    U = triu(matrix, N)
    mD = mulMatrix(D, -1)
    LU = addM(L,U)
    r2 = forward_subD(D,b)
    r = ones(N)
    res = 1
    norm_r = 1
    iteration = 0
    start_time = time.process_time()
    while norm_r > endWhile:
        iteration += 1
        LUr = mulMatrixAndVector(LU,r)
        r1 = forward_subD(mD,LUr)
        r = addV(r1,r2)
        res = mulMatrixAndVector(matrix, r)
        res = subV(res, b)
        norm_r = norm(res)
        if norm_r == -1:
            break
    end_time = time.process_time()
    timee = end_time - start_time
    if o == 1:
        print("Liczba iteracji dla metody Jacobiego z forward_sub dla macierzy diagonalnej", end=' ')
    if o == 1:
        print(iteration)
    if o == 1:
        print("Czas wykonywania z forward_sub dla macierzy diagonalnej: ", end_time - start_time)
    if norm_r != -1:
        if o == 1:
            print("Norma błedu resydualnego: ", norm_r)
    return timee

def GaussSeidl(matrix, N, b, o):
    if o == 1:
        print("\nMetoda Gaussa-Seidla")
    endWhile = 10**-9
    D = diag(matrix, N)
    L = tril(matrix, N)
    U = triu(matrix, N)
    DL = addM(D,L)
    mDL = mulMatrix(DL, -1)
    r2 = forward_sub(DL,b)
    r = ones(N)
    res = 1
    norm_r = 1
    iteration = 0
    start_time = time.process_time()
    while norm_r > endWhile:
        iteration += 1
        Ur = mulMatrixAndVector(U,r)
        r1 = forward_sub(mDL,Ur)
        r = addV(r1,r2)
        res = mulMatrixAndVector(matrix, r)
        res = subV(res, b)
        norm_r = norm(res)
        if norm_r == -1:
            break
    end_time = time.process_time()
    timee = end_time - start_time
    if o == 1:
        print("Liczba iteracji dla metody Gaussa-Seidla", end=' ')
    if o == 1:
        print(iteration)
    if o == 1:
        print("Czas wykonywania: ", end_time - start_time)
    if norm_r != -1:
        if o == 1:
            print("Norma błedu resydualnego dla metody Gaussa-Seidla: ", norm_r)
    return timee

def bezposrednia(matrix, b, o):
    if o == 1:
        print("\nMetoda bezposrednia")
    start_time = time.process_time()
    L, U = lu_factorization(matrix)
    y = forward_sub(L,b)
    x = backword_sub(U, y)
    end_time = time.process_time()
    timee = end_time - start_time
    if o == 1:
        print("czas wykonywania: ", timee)
    res = mulMatrixAndVector(matrix, x)
    res = subV(res, b)
    norm_r = norm(res)
    if o == 1:
        print("Norma błedu resydualnego dla metody bezpośredniej: ", norm_r)
    return timee
   
#########################################################################
# ZADANIA ###############################################################
#########################################################################

#Kacper Puda 188625

#ZADANIE A ##############################################################

N = 925
b = [math.sin((x+1)*(8)) for x in range(N)]
mat = zeros(N)
zadA(mat, N)

#ZADANIE B ##############################################################

GaussSeidl(mat,N,b,1)
Jacobi(mat,N,b,1)
JacobiD(mat,N,b,1)

#ZADANIE C ##############################################################

mat2 = zeros(N)
zadC(mat2, N)
GaussSeidl(mat2,N,b,1)
Jacobi(mat2,N,b,1)

#ZADANIE D ##############################################################

bezposrednia(mat, b,1)

#ZADANIE E ##############################################################
num = [100,500,1000,2000,3000,4000,5000]
g = []
bez = []
j = []
for i in num:
    N = i
    b = [math.sin((x+1)*(8)) for x in range(N)]   
    mat = zeros(N)  
    zadA(mat, N)
    g.append(GaussSeidl(mat,N,b,0))
    j.append(Jacobi(mat,N,b,0))
    if i <= 1000:
        bez.append(bezposrednia(mat,b,0))
        
f = bez[0]
bez.append((20**3) * f )
bez.append((30**3) * f )
bez.append((40**3) * f )
bez.append((50**3) * f )

plt.plot(num, g, label='metoda Gaussa-Seidla')
plt.plot(num, j, label='metoda Jacobiego')
plt.plot(num, bez, label='metoda bezpośrednia')
plt.xlabel('Liczba niewiadomych N')
plt.ylabel('Czas trwania')
plt.title('Wykres czasu trwania funkcji w zależności od ilości iteracji')
plt.legend()
plt.show()
