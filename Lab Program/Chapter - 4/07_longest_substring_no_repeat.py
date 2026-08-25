def length_of_longest_substring(s):
    last={}; left=0; ans=0
    for right,ch in enumerate(s):
        if ch in last and last[ch]>=left: left=last[ch]+1
        last[ch]=right
        ans=max(ans,right-left+1)
    return ans

for s in ["abcabcbb","bbbbb","pwwkew"]:
    print(s, "->", length_of_longest_substring(s))
