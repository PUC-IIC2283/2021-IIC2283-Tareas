from io import BytesIO
from os import read, fstat

def search(l, r, a, b):
    if l > r or a > b: return 0
    ans = -2e18
    m = (l+r) >> 1
    best_k = -1
    valid = False
    for k in range(a, b+1):
        dx = B[k][0] - A[m][0]
        dy = B[k][1] - A[m][1]
        tmp = dx * dy
        if dx > 0 and dy > 0: valid = True
        if tmp > ans:
            ans = tmp
            best_k = k    
    if not valid: ans = 0
    ans = max(ans, search(l, m-1, a, best_k))
    ans = max(ans, search(m+1, r, best_k, b))
    return ans

def main():
    global m, n, A, B
    
    input = BytesIO(read(0, fstat(0).st_size)).readline
    m, n = input().decode().split()
    m = int(m)
    n = int(n)

    A = [None] * m
    B = [None] * n
    for i in range(m):
        x, y = input().decode().split()
        A[i] = (int(x), int(y))
    for i in range(n):
        x, y = input().decode().split()
        B[i] = (int(x), int(y) + 1)
    
    A.sort()
    ref = A[0]
    j = 1
    for i in range(1,m):
        if ref[0] < A[i][0] and ref[1] > A[i][1]:
            A[j] = ref = A[i]
            j += 1
    A = A[:j]

    B.sort(reverse=True)
    ref = B[0]
    j = 1
    for i in range(1,n):
        if ref[0] > B[i][0] and ref[1] < B[i][1]:
            B[j] = ref = B[i]
            j += 1
    B = B[:j]
    B = B[::-1]

    print(search(0, len(A)-1, 0, len(B)-1))

main()