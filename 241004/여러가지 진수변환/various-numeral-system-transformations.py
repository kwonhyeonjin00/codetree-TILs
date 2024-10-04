n, B = map(int, input().split())

arr = []

while True:
    if n < B:
        arr.append(n)
        break

    arr.append(n % B)
    n //= B

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end='')