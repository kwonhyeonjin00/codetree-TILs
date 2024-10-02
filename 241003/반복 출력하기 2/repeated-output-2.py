def z(n):
    if n == 0:
        return 
    z(n-1)
    print("HelloWorld")

n = int(input())
z(n)