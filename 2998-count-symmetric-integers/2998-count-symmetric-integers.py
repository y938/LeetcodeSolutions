class Solution:
    def countDigit(self, n):
        """Return number of digits in 'n'"""
        ans = 0
        while n:
            ans += 1
            n //= 10
        return ans
    
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            digits = self.countDigit(i)
            if not digits & 1:  # if even number, else skip
                temp_sum = 0
                k = 0
                while k != digits//2: # add digits in right half to temp_sum
                    temp_sum += i % 10
                    i //= 10
                    k += 1
                while k != digits: # subtract digits in left half from temp_sum
                    temp_sum -= i % 10
                    i //= 10
                    k += 1
                if temp_sum == 0: # if temp_sum == 0 then sum of digits in left and right halves are equal
                    ans += 1
        return ans