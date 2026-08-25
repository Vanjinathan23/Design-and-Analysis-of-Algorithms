def longest_palindrome(s):
    n=len(s)
    if not s: return ""
    dp=[[False]*n for _ in range(n)]
    start=end=0
    for length in range(1,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j] and (length<=2 or dp[i+1][j-1]):
                dp[i][j]=True
                if length>end-start+1: start,end=i,j
    return s[start:end+1]

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
