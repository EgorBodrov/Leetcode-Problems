class Solution:
    def romanToInt(self, s: str) -> int:
        info = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        res = []
        for i in range(len(s)):
            if i < len(s) - 1 and info[s[i]] < info[s[i+1]]:
                res.append(-1 * info[s[i]])
            else:
                res.append(info[s[i]])
            
        return sum(res)
