class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        i = 0

        while i < len(nums) and i < k:
            heapq.heappush(self.heap, nums[i])
            i += 1

        while i < len(nums):
            heapq.heappushpop(self.heap, nums[i])
            i += 1
        

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
