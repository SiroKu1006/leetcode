class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            cas = 0
            while i > 0:
                if i%2 != 0:
                    cas +=1
                i //= 2
            ans.append(cas)
        return ans