class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums)
        return [element for element,count in store.most_common(k)]
