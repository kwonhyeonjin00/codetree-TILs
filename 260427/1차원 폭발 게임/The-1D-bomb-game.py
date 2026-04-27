n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
def check(numbers):
    t = len(numbers)
    numbers = numbers + [None]

    chk_list = [True] * t

    temp = numbers[0]
    cnt = 0

    # 제거야 할 부분의 인덱스를 chk_list에 False로 표시
    for i in range(t + 1):

        if temp == numbers[i]:
            cnt += 1
        else:
            if cnt >= m:
                for j in range(i - 1, i - 1 - cnt, -1):
                    chk_list[j] = False
            temp = numbers[i]
            cnt = 1
    numbers.pop()

    # chk_list에서 True인 곳만 살리기
    numbers = [num for num, x in zip(numbers, chk_list) if x]

    # True는 그만 해도 된다는 뜻 
    if t == len(numbers):
        return numbers, True
    else:
        return numbers, False
    
is_done = False

while not is_done:
    numbers, is_done = check(numbers)

if numbers:
    print(len(numbers))
    for elem in numbers:
        print(elem)
else:
    print(0)