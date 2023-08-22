class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        arr = []
        i = ord(s[0])
        j = ord(s[3])
        while i!=j+1:
            if s[4]!="1":
                for k in range(int(s[1]), int(s[4])+1):
                    arr.append(chr(i)+str(k))
            else:
                arr.append(chr(i)+"1")
            i+=1
        return arr