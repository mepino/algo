from itertools import permutations
import numpy as np

class Solution:
    def reorganizeString(self, s: str) -> str:      
        list_s = list(s)
        set_s = set(s)
        s_dict = {unique_s:s.count(unique_s) for unique_s in set_s}
        s_count = [s.count(unique_s) for unique_s in set_s]

        # 날려버릴거 먼저 하기        
        if (sum(s_count) - max(s_count)) < (max(s_count) - 1):
            return ""
        if len(s) == 0:
            return ""

        new_s = []

        while s:
            if len(s) == 1:
                if new_s[-1][-1] == s[0]:
                    return ""
                else:
                    return "".join(np.reshape(new_s, -1)) + s
            set_s = set(s)
            s_dict = {unique_s:s.count(unique_s) for unique_s in set_s}
            s_dict_sorted = sorted(s_dict.items(), key=lambda x:x[1], reverse=True)

            try:
                max_char_1 = s_dict_sorted[0][0]
                max_char_2 = s_dict_sorted[1][0]

                new_s.append([max_char_1, max_char_2])
                list_s.remove(max_char_1)
                list_s.remove(max_char_2)

                s = ''.join(list_s)
                if len(s) == 0:
                    return "".join(np.reshape(new_s, -1))
            except:
                return ""