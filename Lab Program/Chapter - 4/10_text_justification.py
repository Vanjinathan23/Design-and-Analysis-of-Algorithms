def full_justify(words, maxWidth):
    res=[]; i=0
    while i<len(words):
        j=i; length=0
        while j<len(words) and length+len(words[j])+(j-i)<=maxWidth:
            length+=len(words[j]); j+=1
        gaps=j-i-1
        if j==len(words) or gaps==0:
            line=" ".join(words[i:j])
            line+=" "*(maxWidth-len(line))
        else:
            spaces=maxWidth-length
            base,extra=divmod(spaces,gaps)
            line=""
            for k in range(i,j-1):
                line+=words[k]+" "*(base+(1 if k-i<extra else 0))
            line+=words[j-1]
        res.append(line); i=j
    return res

words=["This","is","an","example","of","text","justification."]
for line in full_justify(words,16): print(repr(line))
