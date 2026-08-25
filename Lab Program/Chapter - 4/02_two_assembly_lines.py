def assembly_line(a1, a2, t1, t2, e1, e2, x1, x2):
    n = len(a1)
    f1, f2 = [0]*n, [0]*n
    f1[0], f2[0] = e1+a1[0], e2+a2[0]
    for i in range(1, n):
        f1[i] = min(f1[i-1]+a1[i], f2[i-1]+t2[i-1]+a1[i])
        f2[i] = min(f2[i-1]+a2[i], f1[i-1]+t1[i-1]+a2[i])
    return min(f1[-1]+x1, f2[-1]+x2)

a1=[7,9,3,4,8,4]; a2=[8,5,6,4,5,7]
t1=[2,3,1,3,4]; t2=[2,1,2,2,1]
print("Minimum time:", assembly_line(a1,a2,t1,t2,2,4,3,2))
