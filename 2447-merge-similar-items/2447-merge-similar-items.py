class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = items1
        for i in range(len(items1)):
            for j in range(len(items2)):
                if items1[i][0] == items2[j][0]:
                    res[i][1] = items1[i][1] + items2[j][1]
        arr = [i[0] for i in items1]
        for j in items2:
            if j[0] not in arr:
                res.append(j)
        res.sort()
        return res