class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        info = {}
        for letter in magazine:
            if letter in info:
                info[letter] += 1
            else:
                info[letter] = 1
        
        for letter in ransomNote:
            if letter in info and info[letter] > 0:
                info[letter] -= 1
            else: 
                return False
        
        return True