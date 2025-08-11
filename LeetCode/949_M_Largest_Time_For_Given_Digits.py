from typing import List
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        self.maxTime = "00:00" #MINIMUM TIME POSSIBLE
        self.stat = False #TAKE A STATUS VARIABLE WHICH WILL TELL US IF WE FOUND OUR ANSWER OR NOT
        # APPROACH IS TO SORT THE ARRAY IN DESCENDING ORDER AND THEN CREATE PERMUTATIONS, THIS WILL HELP US REACH THE ANSWER FAST
        Map  ={}
        arr.sort(reverse=True)
        for i in range(len(arr)):
            Map[i]=0
        
        def perm(ans):
            if len(ans)==4:
                hr = ''.join(ans[:2])
                mm = ''.join(ans[2:])
                time = hr+':'+mm
                t1 = int(hr)
                t2 = int(mm)
                if t1<=23 and t2<=59:
                    #IF TIME IS VALID ONLY THEN COMPARE
                    if t1>=int(self.maxTime[:2]):
                        if t2>=int(self.maxTime[3:]):
                            self.maxTime = time
                            self.stat = True
                return

            if self.stat == True: return            
            for i in range(0, len(arr)):
                if Map[i]!=1:
                    Map[i]=1
                    ans.append(str(arr[i]))
                    perm(ans)
                    # RETURN IF WE FOUND OUR ANSWER
                    if self.stat == True: return
                    Map[i]=0
                    ans.pop()
        perm([])
        
        if self.maxTime!="00:00" or(self.maxTime=="00:00" and self.stat==True): return (self.maxTime)
        else: return ""

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        import itertools
        bestTime = None
        for i in itertools.permutations(arr):
            a,b,c,d = i
            h = int(str(a)+str(b))
            if h >= 24: continue
            m = int(str(c)+str(d))
            if m >= 60: continue
            
            if bestTime == None or h > bestTime[0] or (h == bestTime[0] and m > bestTime[1]):
                bestTime = [h,m]
        if bestTime == None: return ""
        a = str(bestTime[0])
        b = str(bestTime[1])
        if len(a) == 1: a = "0" + a
        if len(b) == 1: b = "0" + b
        s = a + ":" + b
        return s