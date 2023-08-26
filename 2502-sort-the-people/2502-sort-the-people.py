class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = []
        b = []
        for i  in range(len(names)):
            a.append([names[i],heights[i]])
        a.sort(key= lambda x:x[1])
        a.reverse()
        for i in a:
            b.append(i[0])
        return b

        