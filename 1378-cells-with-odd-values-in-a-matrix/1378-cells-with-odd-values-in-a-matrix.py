class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        a = []
        count = 0
        for i in range(m):
            a.append([])

        for i in range(m):
            for j in range(n):
                a[i].append(0)

        for i in indices:
            for j in range(len(i)):
                if j == 0:
                    for k in range(len(a[i[j]])):
                        a[i[j]][k]+=1
                else:
                    for k in range(len(a)):
                        a[k][i[1]]+=1
        
        for i in a:
            for j in i:
                if j%2 !=0:
                    count +=1
        return count