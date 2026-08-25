class WordFilter:
    def __init__(self, words):
        self.words=words
    def f(self, pref, suff):
        for i in range(len(self.words)-1,-1,-1):
            if self.words[i].startswith(pref) and self.words[i].endswith(suff):
                return i
        return -1

wf=WordFilter(["apple"])
print(wf.f("a","e"))
