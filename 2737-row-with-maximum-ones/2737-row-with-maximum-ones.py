from collections import Counter
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        arr = [[] for i in mat]
        for i in range(len(mat)):
            for j in mat[i]:
                if j== 1:
                   arr[i].append(j)
        a  = [len(i) for i in arr]
        return [a.index(max(a)), max(a)]