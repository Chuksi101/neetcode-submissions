class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last2 = n-1
        last1 = m-1
        back = m+n-1

        while last2 >= 0:
            if last1 >= 0 and nums1[last1] > nums2[last2]:
                nums1[back] = nums1[last1]
                last1 -= 1
            else:
                nums1[back] = nums2[last2]
                last2 -= 1
            back -= 1