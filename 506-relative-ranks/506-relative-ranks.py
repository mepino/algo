class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_dict = {val:i for i, val in enumerate(score)}
        score_copy = score.copy()

        for i, info in enumerate(sorted(score_dict.items())):
            rank = len(score) - i
            val = info[0]
            ind = info[1]

            if rank == 1:
                score_copy[ind] = "Gold Medal"
            elif rank == 2:
                score_copy[ind] = "Silver Medal"
            elif rank == 3:
                score_copy[ind] = "Bronze Medal"
            else:
                score_copy[ind] = str(rank)
        return score_copy