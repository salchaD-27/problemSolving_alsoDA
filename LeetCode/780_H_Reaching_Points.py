# class Solution:
#     def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
#         def fs(x, y):
#             if (x,y)==(tx,ty): return True
#             if x>tx or y>ty: return False
#             return fs(x, x+y) or fs(x+y, y)
#         return fs(sx, sy)

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy: return True
            if tx > ty:
                if ty > sy: tx %= ty
                else: return (tx - sx) % ty == 0
            else:
                if tx > sx: ty %= tx
                else: return (ty - sy) % tx == 0
        return False