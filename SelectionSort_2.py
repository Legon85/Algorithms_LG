a = [5, 3, 4, 9, 7, 6, 2, 1, 8]
N = len(a)

# Selection sort  O(n**2)
for i in range(N - 1):
    m = a[i]
    p = i
    for j in range(i + 1, N):
        if m > a[j]:
            m = a[j]
            p = j

    if p != i:
        t = a[i]
        a[i] = a[p]
        a[p] = t

print(a)
