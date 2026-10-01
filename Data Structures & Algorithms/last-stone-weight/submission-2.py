class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            left = -heapq.heappop(heap)
            right = -heapq.heappop(heap)
            if left != right:
                heapq.heappush(heap, -abs(left-right))

        return -heap[0] if heap else 0