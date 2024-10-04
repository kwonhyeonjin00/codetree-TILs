n = input()
binary = []

for i in n:
    binary.append(i)
num = 0

for i in range(len(n)):
    num = num * 2 + int(binary[i])

num *= 17

arr = []

while True:
    if num < 2:
        arr.append(num)
        break

    arr.append(num % 2)
    num //= 2

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end='')