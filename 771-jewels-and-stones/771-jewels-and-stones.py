from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        
        my_jewels = 0
        
        for jewel in jewels:
            my_jewels += counter[jewel]
            
        return my_jewels