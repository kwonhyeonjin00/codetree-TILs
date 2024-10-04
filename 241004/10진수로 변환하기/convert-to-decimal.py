n = input()

binary = []

for i in n:
    binary.append(i)
num = 0

for i in range(len(n)):
    num = num * 2 + int(binary[i])

print(num)