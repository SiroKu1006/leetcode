import numpy as np

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if sum(1 for i in trust if i[1] == n) == n-1 :
            return True
        else:
            return False
        
        

# s = Solution()
# print(s.findJudge(3,[[1,3],[2,3]]))
a = [[1,3],[2,3]]
c = np.where(a)