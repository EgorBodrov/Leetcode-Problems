class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        info = {k: sum(v) for k, v in enumerate(mat)}
        res_dict = dict(sorted(info.items(), key=lambda item: item[1]))
        
        return list(res_dict.keys())[:k]
        
        