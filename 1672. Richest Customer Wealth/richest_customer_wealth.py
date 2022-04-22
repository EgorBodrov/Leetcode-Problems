class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthes = [sum(x) for x in accounts]
        
        return max(wealthes)
