def Maxi(nums,k):
    zc=0
    max_len=0
    left=0
    n=len(nums)
    for right in range(n):
        if nums[right]==0:
            zc+=1
        while zc>k:
            if nums[left]==0:
                zc-=1
            left+=1
        curr_len=right-left+1
        if curr_len>max_len:
            max_len=curr_len
    return max_len
