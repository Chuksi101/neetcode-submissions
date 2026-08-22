class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        '''
        result = []
        sortedNums = sorted(nums)
        print(sortedNums)
        for i in range(len(nums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            if sortedNums[i] > 0:
                break
            
            j,k = i+1,len(nums)-1
            while j < k:
                total = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if total == 0:
                    result.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while k > i and sortedNums[k] == sortedNums[k-1]:
                        k -= 1
                    k -= 1
                    while j < len(nums)-1 and sortedNums[j] == sortedNums[j+1]:
                        j += 1
                    j += 1

                elif total > 0:
                    while k > i and sortedNums[k] == sortedNums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    while j < len(nums) and sortedNums[j] == sortedNums[j+1]:
                        j += 1
                    j += 1

        return result