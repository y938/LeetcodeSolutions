class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count =0
        for i in range(low, high+1):
            if len(str(i)) % 2 == 0:
                mid = int(len(str(i))) // 2
                s = str(i)
                x = [int(j) for j in s[:mid]]
                y = [int(j) for j in s[mid:len(str(i))]]
                if sum(x)==sum(y):
                    count +=1
        return count
