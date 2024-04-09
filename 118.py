class Solution:   
    
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        for i in range(3,numRows+1):
            cas = [1]
            for j in range(1,i-1):
                cas.append(ans[i-2][j-1]+ans[i-2][j])
            cas.append(1)
            ans.append(cas)
        return ans

ans = Solution()
print(ans.generate(5))