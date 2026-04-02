def kth_max_sum(nums,k):
    n=len(nums)
    window_sum=0
    for i in range(k):
        window_sum+=nums[i]
    max_sum=window_sum
    for i in range(k,n):
        window_sum+=nums[i]
        window_sum-=nums[i-k]
        if window_sum>max_sum:
            max_sum=window_sum
    return max_sum
print(kth_max_sum([2,1,5,1,3,2],3))

