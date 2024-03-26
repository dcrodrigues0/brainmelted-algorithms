# LeetCode 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) <= 0:
            return []

        duplicateds = []
        nums.sort()
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                duplicateds.append(nums[i])
        return duplicateds