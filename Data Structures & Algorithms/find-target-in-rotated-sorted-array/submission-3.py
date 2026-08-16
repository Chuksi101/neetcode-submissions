class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            
            current = nums[mid]
            if current == target:
                return mid
            elif current < nums[right]:
                if target > current and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                # Left side is sorted
                if target < current and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1