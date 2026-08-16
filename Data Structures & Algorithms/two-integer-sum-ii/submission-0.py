class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            '''
            if num[left] + num[right] == target:
                return [left, right]
            elif >:
                while left < right and num[left] != num[left + 1]:
                    left += 1
            else:
                repeat above for right (using -1 & right -= 1)
            '''
            print(left)
            print(right)
            if numbers[left] + numbers[right] == target:
                return [left + 1,right + 1]
            elif numbers[left] + numbers[right] < target:
                left +=1
                while left < right and numbers[left] == numbers[left - 1]:
                    left +=1
            else:
                right -= 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -=1
