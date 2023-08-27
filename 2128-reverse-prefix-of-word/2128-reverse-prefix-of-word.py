class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            a = word.index(ch)
            b = []
            while a>=0:
                b.append(word[a])
                a-=1
            c = word.index(ch)
            for i in range(c+1,len(word)):
                b.append(word[i])
            return "".join(b)
        else:
            return word