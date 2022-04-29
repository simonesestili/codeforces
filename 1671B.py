t = int(input())

def valid(arr, l):
    for x in arr:
        if abs(x - l) > 1: return False
        l += 1
    return True

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if valid(nums, nums[0]-1) or valid(nums, nums[0]) or valid(nums, nums[0]+1):
        print('YES')
    else:
        print('NO')

