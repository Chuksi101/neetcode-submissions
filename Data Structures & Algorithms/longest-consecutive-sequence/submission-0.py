class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        if array is len 0 return 0
        We can convert the array to a set
        Initialize a max result (maxResult = 0)
        Then we check if num-1 does not exist (to find the start of the sequence) and keep checking for +1 (increasing a temp result if +1 in set).
        When you're done with your walk, check and potentially re-assign maxResult
        '''
        if nums == []:
            return 0
        store = set(nums)
        maxResult = 0
        for i in store:
            currentValue = i
            if currentValue-1 not in store:
                currentLength = 1
                while currentValue + 1 in store:
                    currentLength += 1
                    currentValue += 1
                maxResult = max(maxResult, currentLength)
        return maxResult
