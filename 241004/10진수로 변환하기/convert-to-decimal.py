n = input()

binary = []

for i in n:
    binary.append(i)
num = 0

for i in range(5):
    num = num * 2 + int(binary[i])

print(num)