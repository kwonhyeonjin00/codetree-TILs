n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
x = 0
for i in range(0, n):
    if nums[i] + nums[2 * n - 1 - i] > x:
        x = nums[i] + nums[2 * n - 1 - i]

print(x)