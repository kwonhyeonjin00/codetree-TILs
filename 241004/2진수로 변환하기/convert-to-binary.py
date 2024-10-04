n = int(input())

arr = []

while True:
    if n < 2:
        arr.append(n)
        break

    arr.append(n % 2)
    n //= 2

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end='')