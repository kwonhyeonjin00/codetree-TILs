n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
print(*nums)
nums = nums[::-1]
print(*nums)