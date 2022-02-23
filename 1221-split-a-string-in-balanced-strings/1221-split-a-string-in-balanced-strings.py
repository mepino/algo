class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        pair_list = []
        for element in s:
            pair_list.append(element)

            no_l = pair_list.count('L')
            no_r = pair_list.count('R')

            if no_l == no_r:
                count+= 1
                pair_list=[]
        return count
