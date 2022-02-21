class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result_list = []
        
        set_nums = set(nums)
        for i in range(len(nums)):
            if i+1 not in set_nums:
                result_list.append(i+1)
        return result_list