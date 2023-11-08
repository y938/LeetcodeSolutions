class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy:
            if t==1: return False
            else: return True
        x_dif = abs(sx-fx)
        y_dif = abs(sy-fy)
        if x_dif <= t and y_dif <= t :
            return True
        return False