class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n_set_sol = 2 ** k
        hash_s_list = set()
        
        for i in range(len(s)-k+1):
            hash_s_list.add(s[i:i+k])
            
        return len(hash_s_list) == n_set_sol