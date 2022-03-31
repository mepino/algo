from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        dup_list = set()

        for i, char in enumerate(s):
            if char in od.keys():
                dup_list.add(char)
            else:
                od[char] = i

        sol_list = set(od.keys()) - dup_list
        result_list = [[key, value] for key, value in od.items() if key in sol_list]
        
        try:
            result = sorted(result_list, key=lambda x:x[1], reverse=False)[0][1]
            return result
        except:
            return -1