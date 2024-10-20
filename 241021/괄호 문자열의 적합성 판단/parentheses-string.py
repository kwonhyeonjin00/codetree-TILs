def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
        elif arr[i] == ')':
            if not stack:
                return "No"
            else:
                stack.pop()
    if stack:
        return "No"
    return "Yes"

arr = list(input())
stack = []
print(check(arr))