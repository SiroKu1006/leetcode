

class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        
        return 5 + 4*((n-1)**2) + 3*((n-1)**3) + 2*((n-1)**4) + ((n-1)**5)

ans = Solution()
print(ans.countVowelStrings(1),5)
print(ans.countVowelStrings(2),15)
print(ans.countVowelStrings(33),66045)