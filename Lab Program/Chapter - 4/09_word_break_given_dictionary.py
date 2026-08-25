dictionary={"i","like","sam","sung","samsung","mobile","ice","cream","icecream","man","go","mango"}

def can_segment(s):
    dp=[False]*(len(s)+1); dp[0]=True
    for i in range(1,len(s)+1):
        dp[i]=any(dp[j] and s[j:i] in dictionary for j in range(i))
    return dp[-1]

for s in ["ilike","ilikesamsung"]:
    print(s, "->", "Yes" if can_segment(s) else "No")
