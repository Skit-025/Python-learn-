def Long_substring(s:str)->int:
    seen={}
    max_len,n,left=0,len(s),0
    for right in range(n):
        if s[right] in seen and seen[s[right]]>=left:
            left=seen[s[right]]+1
        seen[s[right]]=right
        curr_len=right-left+1
        if curr_len>max_len:
            max_len=curr_len
    return max_len
print(Long_substring("abcabcbb"))