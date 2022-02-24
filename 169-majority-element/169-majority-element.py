class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        max_val = 0
        for element in set(nums):

          n_count = nums.count(element)
          print(element, n_count)
          if n_count > max_count:
            max_count = n_count
            max_val = element
        return max_val