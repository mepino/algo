class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_nums = []

        for i in range(len(nums)):
            # print(nums[nums[i]])
            new_nums.append(nums[nums[i]])
        return new_nums