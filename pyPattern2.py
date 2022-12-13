def pyStar(n):
    L=[]
    for i in range (1,n+1):
        L.append("*" *i)
    print('\n'.join(L))
n=5
pyStar(n)