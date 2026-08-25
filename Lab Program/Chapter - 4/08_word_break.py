def word_break(s, wordDict):
    words=set(wordDict)
    dp=[False]*(len(s)+1); dp[0]=True
    for i in range(1,len(s)+1):
        dp[i]=any(dp[j] and s[j:i] in words for j in range(i))
    return dp[-1]

print(word_break("leetcode",["leet","code"]))
print(word_break("applepenapple",["apple","pen"]))
print(word_break("catsandog",["cats","dog","sand","and","cat"]))
