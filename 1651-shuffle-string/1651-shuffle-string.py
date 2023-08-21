class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [_ for _ in indices]
        for i,j in zip(indices,s):
            arr[i] = j
        return "".join(arr)