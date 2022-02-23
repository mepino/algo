class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pointer = 0
        counter = 0
        while pointer < len(nums)-1:
            left_val = nums[pointer]
            pointer += 1
            p_val = nums[pointer]

            if p_val > left_val:
                continue
            else:
                temp_counter = left_val - p_val + 1
                counter += temp_counter
                nums[pointer] = p_val + temp_counter
        return counter
