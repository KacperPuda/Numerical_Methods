
import numpy as np

def spline_interpolation(x, y):
    n = len(x) - 1
    h = np.diff(x)
    # Tworzenie macierzy A
    A = np.zeros((n*4,n*4))
    r = np.zeros(n*4)
    j = 0
    k = 0
    l = 0
    for i in range(n):
        A[k][j] = 1
        r[k] = y[l]
        l += 1
        j+=4
        k+=2
    p = 0
    k = 1
    l = 1
    for i in range(n):
        for j in range(4):
            A[k][j + p] = 1*(h[i]**j)
        p+=4
        r[k] = y[l]
        k+=2
        l += 1

    k = n*2
    p = 0
    for i in range(n-1):
        A[k][1+p] = 1
        A[k][2+p] = (h[i]**1)*2
        A[k][3+p] = (h[i]**2)*3
        A[k][5+p] = -1
        A[k+1][2+p] = 2
        A[k+1][3+p] = h[i]*6
        A[k+1][6+p] = -2
        k+=2
        p+=4

    A[n*4-1][n*4-2] = 2
    A[n*4-1][n*4-1] = h[len(h)-1]*6
    A[n*4-2][2] = 2

    c = np.linalg.solve(A, r)

    return c

def evaluate_spline(x, spline, new_x):
    # Znajdź indeks odcinka, do którego należy nowy punkt
    index = 0
    for i in range(len(x)-1):
        if new_x > x[i+1]:
            index += 1
        elif new_x == i:
            break
    if index == len(x) - 1:
        index -= 1
    delta_x = new_x - x[index]
    y_value = spline[4*(index)] + spline[4*(index)+1] * delta_x + spline[4*(index)+2] * delta_x**2 + spline[4*(index)+3] * delta_x**3
    return y_value