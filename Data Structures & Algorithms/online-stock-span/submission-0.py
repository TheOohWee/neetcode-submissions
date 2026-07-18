class StockSpanner:

    def __init__(self):
        self.p = []

    def next(self, price: int) -> int:
        i = 1
        while self.p and self.p[-1][0] <= price:
            popped = self.p.pop()
            i += popped[1]

        self.p.append((price, i))
        return i



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)