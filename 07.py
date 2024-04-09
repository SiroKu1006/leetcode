class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            k = x[1:]
            k = k[::-1]
            return int(x+k)
        else:
            return int(x[::-1])