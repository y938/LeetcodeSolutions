class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        arr=[]
        for i in s:
            arr.append(i)

        count = 0
        for i in arr:
            if num % int(i)==0:
                count+=1
            else:
                continue
        return count