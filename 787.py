# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
import numpy as np
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = np.zeros((n,n))
        for a in flights:
            graph[a[0]][a[1]] = a[2]
        
        ans = self.go(graph,[src],dst,k,0)
        return ans
    def go(self,graph,walked:list,ed,k,price):
        if len(walked) - 2 == k :
            if walked[-1] == ed:
                return price
        for i in range(len(graph[walked[-1]])):
            if graph[walked[-1]][i] != 0 and i not in walked:
                walked.append(i)
                price += graph[walked[-1]][i]
                self.go(graph,walked,ed,k,price)





s = Solution()
ans = s.findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0, 3, 1)
print(ans)
