n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
sort_word = sorted(word)
for x in sort_word:
    print(x)