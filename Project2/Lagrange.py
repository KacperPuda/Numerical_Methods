def Lagrange(x_v,y_v,x):
    n = len(x_v)
    w = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if j != i:
                l  *= (x-x_v[j])/(x_v[i]-x_v[j])
        w += y_v[i]*l
    return w
            