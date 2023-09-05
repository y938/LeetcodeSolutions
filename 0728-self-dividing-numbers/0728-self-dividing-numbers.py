class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a=[]
        b = True
        for i in range(left,right+1):
            if i >0 and i<10:
                a.append(i)
            else:
                if "0" in str(i):
                    continue
                else:
                    for j in str(i):
                        if i%int(j)==0:
                            b = True
                        else:
                            b = False
                            break
                if b:
                    a.append(i)
        return a

        