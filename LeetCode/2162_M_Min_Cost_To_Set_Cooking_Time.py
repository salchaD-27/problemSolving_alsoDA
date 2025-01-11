# def possTimeCombs(targetSeconds):
#     res=[]
#     mins=targetSeconds//60
#     secs=targetSeconds-mins*60
#     time=mins*100 + secs
#     res.append(str(time))
#     res.append(str(time-100+60))
#     return res

# def possTimeCombs(targetSeconds): return [str(((targetSeconds//60)*100)+(targetSeconds-(60*(targetSeconds//60)))), str((((targetSeconds//60)*100)-100)+(60+(targetSeconds-(60*(targetSeconds//60)))))]
# def minCostSetTime(startAt, moveCost, pushCost, targetSeconds):
#     cost=float('inf')
#     possTimes=possTimeCombs(targetSeconds)
#     for time in possTimes:
#         timeSet=set()
#         timeSet.add(startAt)
#         for i in range(len(time)):
#             timeSet.add(i)
#         costToMove=len(timeSet)*moveCost
#         costToPush=len(time)*pushCost
#         tempCost=costToMove+costToPush
#         if tempCost<cost: cost=tempCost
#     return cost

class Solution:
    def __init__(self): pass

    def possTimeCombs(self, targetSeconds: int) -> list:
        combinations = []
        minutes = targetSeconds//60
        seconds = targetSeconds%60
        if minutes < 100: combinations.append(f"{minutes * 100 + seconds}")
        if minutes > 0 and seconds + 60 < 100: combinations.append(f"{(minutes - 1) * 100 + seconds + 60}")
        return combinations

    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        cost = float('inf')
        possTimes = self.possTimeCombs(targetSeconds)
        for time in possTimes:
            time = time.lstrip('0') 
            currentCost = 0
            prevDigit = str(startAt)

            for digit in time:
                if digit != prevDigit: currentCost += moveCost 
                currentCost += pushCost 
                prevDigit = digit
            cost = min(cost, currentCost)
        return cost