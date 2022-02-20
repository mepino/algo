class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            try:
                nums.index(i+1)
            except:
                return i+1
        return 0