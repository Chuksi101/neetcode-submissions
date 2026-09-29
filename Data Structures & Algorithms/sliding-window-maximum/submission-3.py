class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(k-1):
            heapq.heappush(heap,(-nums[i], i))

        for r in range(k-1,len(nums)):
            heapq.heappush(heap,(-nums[r], r))
            currMax = heap[0]
            while r - currMax[1] >= k:
                heapq.heappop(heap)
                currMax = heap[0]
            res.append(-currMax[0])


        return res
