class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        def rebalance(larger, smaller):
            curr = heapq.heappop(larger)
            curr *= -1
            heapq.heappush(smaller, curr)

        if self.big and num > self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) > len(self.big) + 1:
            rebalance(self.small, self.big)
        elif len(self.small) < len(self.big) - 1:
            rebalance(self.big, self.small)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        elif len(self.small) < len(self.big):
            return self.big[0]
        else:
            return (-self.small[0] + self.big[0])/2