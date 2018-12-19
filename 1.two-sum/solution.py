#O(n^2)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length-1):
            first = nums[i]
            expected = target - first
            for j in range(i+1, length):
                if nums[j] == expected:
                    return [i, j]
