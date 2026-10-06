class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points[:k]:
            dist = ((x ** 2) + (y ** 2)) ** 0.5
            heapq.heappush(heap,(-dist, (x,y)))
        for x,y in points[k:]:
            dist = ((x ** 2) + (y ** 2)) ** 0.5
            heapq.heappushpop(heap,(-dist, (x,y)))
        return [x[1] for x in heap]