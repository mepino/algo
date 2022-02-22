class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        new_nums = []
        copy_nums = nums.copy()

        for num in nums:
            if num%2 == 0:
                new_nums.append(num)
                copy_nums.remove(num)
                
        return new_nums + copy_nums
