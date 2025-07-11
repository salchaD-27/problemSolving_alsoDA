# class StockSpanner:
#     def __init__(self): self.stocks=[]
#     def next(self, price: int) -> int:
#         span=1
#         for i in range(len(self.stocks)-1,-1,-1):
#             if self.stocks[i]<=price: span+=1
#             else: break
#         self.stocks.append(price)
#         return span

class StockSpanner:
    def __init__(self): self.stocks=[]
    def next(self, price: int) -> int:
        span = 1
        while self.stocks and self.stocks[-1][0] <= price:
            span += self.stocks.pop()[1]
        self.stocks.append((price, span))
        return span