class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        nums = sorted(nums, reverse=True)
        
        return str(nums[k-1])