from itertools import permutations
import numpy as np

class Solution:
    def minimumSum(self, num: int) -> int:
        print(num)
        str_num = str(num)
        new_str_num = []
        for str_element in str_num:
            new_str_num.append(str_element)

        n_length = len(new_str_num)
        n_1 = n_length // 2
        n_2 = n_length - n_1
        
        min_sum = np.inf

        for word_1 in list(permutations(new_str_num, n_1)):
            word_maker = new_str_num.copy()

            # word_1에 있는 원소 삭제
            for ele_1 in word_1:
                word_maker.remove(ele_1)

            # 새로운 word_maker로 word_2 만들기
            for word_2 in list(permutations(word_maker, n_2)):
                word_1_result = "".join(word_1)
                word_2_result = "".join(word_2)

                cand_min_sum = int(word_1_result)+int(word_2_result)
                if cand_min_sum < min_sum:
                    min_sum = cand_min_sum
                    
        return min_sum