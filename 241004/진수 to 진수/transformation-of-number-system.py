a, b = map(int, input().split())
n = input()

binary = []
for i in n:
    binary.append(i)

num = 0

for i in range(len(n)):
    num = num * a + int(binary[i])

arr = []

while True:
    if num < b:
        arr.append(num)
        break

    arr.append(num % b)
    num //= b

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end='')