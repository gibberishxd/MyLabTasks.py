def akk(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return akk(m-1, 1)
    elif m>0 and n>0:
        return akk(m-1, akk(m, n-1))
    else:
        return 0
m = int(input("Enter m"))
n = int(input("Enter n"))

print(akk(m,n))