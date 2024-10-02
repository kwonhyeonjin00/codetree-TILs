def print_n_lines(n):
    a = 1
    for i in range(n):
        for j in range(n):
            print(a, end=' ')
            a += 1
            if a > 9:
                a -= 9
        print()


row_num = int(input())
print_n_lines(row_num)