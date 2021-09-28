from copy import deepcopy
p = int(1e9)+7


def id(n: int):
    a = [n*[0] for _ in range(n)]
    for i in range(n):
        a[i][i] = 1
    return a


def mult(a, b):
    n = len(a)
    c = [n*[0] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j]=sum((a[i][k]*b[k][j])%p for k in range(n))%p
    return c


def mpow(a,n):
    if n == 0:
        return id(len(a))
    else:
        res = id(len(a))
        pot = a
        while n > 0:
            if n % 2==1:
                res = mult(res, pot)
            n //= 2
            pot = mult(pot, pot)
        return res

A = [[0,2,2,1],
     [2,0,0,1],
     [2,0,0,1],
     [1,1,1,0]]

n = int(input())

M_out = mpow(A,n)
print(sum((sum(c)%p for c in M_out))%p)
