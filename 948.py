class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        score = 0
        n = len(tokens)
        max_score = 0
        left = 0
        right = n-1
        tokens.sort()
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score+=1
                max_score = max(max_score,score)
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break

        return max_score
    
s = Solution()
print(s.bagOfTokensScore([100,200,300,400],200))