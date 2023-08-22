class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i=0
        count=0
        if ruleKey=="type":
            i=0
        elif ruleKey=="color":
            i=1
        else:
            i=2
        for j in items:
            if j[i]==ruleValue:
                count+=1
        return count