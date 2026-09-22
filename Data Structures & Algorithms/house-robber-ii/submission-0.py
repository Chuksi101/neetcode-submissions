class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        - Assume its the regular rob house recurrence relation
            - The caveat is that you would need two arrays:
                -> One for skipping the last house
                -> one for skipping the first house
            - return max between both
        '''

        if len(nums) < 2:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[1],nums[0])
        dpl = [0 for _ in nums]
        dpf = [0 for _ in nums]
        dpl[0], dpl[1] = nums[0], max(nums[1],nums[0])
        dpf[0], dpf[1] = 0, nums[1]

        for i in range(2, len(nums)-1):
            dpl[i] = max(nums[i] + dpl[i-2], dpl[i-1])
        
        for i in range(2, len(nums)):
            dpf[i] = max(nums[i] + dpf[i-2],dpf[i-1])

        return max(dpf[-1], dpl[-2])