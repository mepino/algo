class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for element in set(nums):
            if nums.count(element) != 2:
                return element