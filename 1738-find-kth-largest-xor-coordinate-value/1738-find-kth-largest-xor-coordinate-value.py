# import numpy as np
# class Solution:
#     def XOR(self, xor_list:List) -> int:
#         if len(xor_list) == 1:
#             return xor_list[0]
#         else:
#             return xor_list[0] ^ self.XOR(xor_list[1:])
        
#     def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
#         matrix = np.array(matrix)
#         m, n = matrix.shape
        
#         matrix_xor = []

#         for i in range(m):
#             for j in range(n):
#                 source_list = matrix[:i+1, :j+1].reshape(-1)
#                 matrix_xor.append(self.XOR(source_list))
                
#         return sorted(matrix_xor, reverse=True)[k-1]

class Solution:
    def kthLargestValue(self, A, k):
        row, col = len(A), len(A[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = A[0][0]
        
        for c in range(1, col):
            dp[0][c] = A[0][c]^dp[0][c-1]
        
        for r in range(1, row):
            dp[r][0] = A[r][0]^dp[r-1][0]
        
        for r in range(1, row):
            for c in range(1, col):
                dp[r][c] = dp[r][c-1]^dp[r-1][c]^dp[r-1][c-1]^A[r][c]
        
        array = []
        for i in range(row):
            for j in range(col):
                array.append(dp[i][j])
        
        if len(array) < k: return 0
        array.sort(reverse=True)
        return array[k-1]