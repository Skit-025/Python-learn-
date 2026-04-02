def Min_subarray(nums,target):
    n=len(nums)
    left=0
    curr_sum=0
    min_len=n+1
    for right in range(n):
        curr_sum+=nums[right]
        while curr_sum>=target:
            curr_len=right-left+1
            if curr_len<min_len:
                min_len=curr_len
            curr_sum-=nums[left]
            left+=1
    if min_len==n+1:
        return 0
    else:
        return min_len
print(Min_subarray([2,3,1,2,4,3],7))