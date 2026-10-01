class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            left = -heapq.heappop(heap)
            right = -heapq.heappop(heap)
            if left != right:
                temp = abs(left-right)
                heapq.heappush(heap, -temp)

        return -heap[0] if heap else 0