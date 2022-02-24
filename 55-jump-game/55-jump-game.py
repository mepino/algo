class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     nums.reverse()
    #     while len(nums) > 1:
    #         i_list = [0 if val-i >= 0 else -1 for i, val in enumerate(nums)]
    #         try:
    #           i_list.index(0)
    #           i_list.reverse()
    #           new_start = len(i_list) - i_list.index(0) - 1
    #           if new_start == 0:
    #             return False
    #           nums = nums[new_start:]
    #         except:
    #           return False
    #     return True
#         nums.reverse()
#         while len(nums) > 1:
#           i_list = []

#           for i, val in enumerate(nums):
#             if i == 0:
#               continue
#             if val-i >= 0:
#               i_list.append(i)
#           if len(i_list) == 0:
#             return False
#           new_start = max(i_list)
#           new_nums = nums[new_start:]
#           if new_nums == nums:
#             return False
#           nums = new_nums
#         return True      

    def canJump(self, nums):
        max_i = 0
        for i, n in enumerate(nums):
          if i > max_i:
            return False
          max_i = max(max_i, i+n)
        return True