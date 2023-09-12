class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        arr = []
        for i in range(n+1):
            a = bin(i)
            for i in a:
                if i =="1":
                    count +=1
            arr.append(count)
            count = 0
        return arr

        