class Solution:
    def climbStairs(self, n):
        step_list = [0 for i in range(n+1)]

        step_list[0], step_list[1] = 1, 1

        for i in range(2, n+1):
            step_list[i] = step_list[i-1] + step_list[i-2]
            
        return step_list[-1]