k, n = map(int, input().split())
answer = []

def answer_print():
    for elem in answer:
        print(elem, end=' ')
    print()

def choose(curr_num):
    if curr_num == n+1:
        answer_print()
        return

    for i in range(1, k+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return
choose(1)