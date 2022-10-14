class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        min_boundary = -1

        while (left <= right):
            mid = (left + right)//2

            if (nums[mid] <= nums[-1]):
                min_boundary = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[min_boundary]
