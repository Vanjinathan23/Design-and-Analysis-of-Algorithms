def str_str(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

print(str_str("sadbutsad", "sad"))   # 0
print(str_str("leetcode", "leeto"))  # -1
