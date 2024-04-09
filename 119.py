class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex +=1
        ans = [[0],[1],[1,1]]
        if rowIndex == 1:
            return [[1]]
        elif rowIndex == 2:
            return [[1,1]]
        for i in range(3,rowIndex+1):
            cas = [1]
            for j in range(1,i-1):
                cas.append(ans[i-1][j-1]+ans[i-1][j])
            cas.append(1)
            ans.append(cas)
        ans.pop(0)
        return ans[-1]
    
ans = Solution()
print(ans.getRow(3))
