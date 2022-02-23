from itertools import permutations

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        source = [x for x in range(len(s)+1)]
        s = s.replace("D", "0")
        s = s.replace("I", "1")

        score_acc = 0
        total_acc = [0 for x in range(len(s)+1)]

        for i, value in enumerate(s):
          weight = i+1

          if value == "0":
            score_pre = -1 * weight
          else:
            score_pre = 1 * weight
          score_acc += score_pre
          total_acc[i+1] = score_acc

        score_dict = {ind:val for ind, val in enumerate(total_acc)}
        sorted_score_dict = sorted(score_dict.items(), key=lambda x:x[1])

        target = [0 for x in range(len(s)+1)]

        for t, i in enumerate(sorted_score_dict):
          target[i[0]] = source[t]

        return target