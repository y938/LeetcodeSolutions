class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if arrivalTime + delayedTime == 24:
            return 0
        elif arrivalTime + delayedTime > 24:
            return (arrivalTime + delayedTime) - 24
        return arrivalTime + delayedTime