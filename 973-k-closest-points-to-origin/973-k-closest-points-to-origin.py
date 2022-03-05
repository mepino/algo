class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [x**2 + y**2 for x, y in points]
        dist_dict = {i:dist for i, dist in enumerate(dists)}
        sorted_dist_dict = sorted(dist_dict.items(), key=lambda x:x[1])
        sorted_index = [index for index, _ in sorted_dist_dict]
        selected_indexes = sorted_index[:k]
        
        result = [points[selected_index] for selected_index in selected_indexes]
        return result