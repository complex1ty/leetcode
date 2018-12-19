# O(n) using hash map
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        hashMap = {}
        for i in range(length):
            num = nums[i]
            compl = target - num
            if compl in hashMap:
                return [hashMap[compl], i]
            hashMap[num] = i