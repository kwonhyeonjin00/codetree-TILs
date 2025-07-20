word1 = input()
word2 = input()

# Please write your code here.
word1 = sorted(word1)
word2 = sorted(word2)
c = 2

if len(word1) != len(word2):
    print("No")
else:
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            print("No")
            c = 0
            break
        else:
            c = 1

if c == 1:
    print("Yes")