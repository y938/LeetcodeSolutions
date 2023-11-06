class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        a = [i for i in range(len(boxes)) if boxes[i]=="1"]
        b = []
        count = 0
        for j in range(len(boxes)):
            for i in a:
                if i != j:
                    count+=abs(i-j)
            b.append(count)
            count=0
        return b