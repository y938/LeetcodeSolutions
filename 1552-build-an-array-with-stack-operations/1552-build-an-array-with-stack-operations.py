from collections import deque
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = deque()
        push_pop = deque()
        for i in range(1,n+1):
            if list(stack)==target:
                break
            else:
                if i in target:
                    stack.append(i)
                    push_pop.append("Push")
                else:
                    push_pop.append("Push")
                    push_pop.append("Pop")
        return push_pop