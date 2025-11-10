n = int(input())
nums = list(map(int, input().split()))
mini = nums.index(min(nums))
maxi = nums.index(max(nums))
if mini > maxi:
    mini, maxi = maxi, mini
sum = 0
for num in nums:
    if num > 0:
        sum = sum + num
pr = 1
for num in nums[mini+1:maxi]:
    pr = pr * num
print(sum, pr)