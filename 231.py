class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0:
            return False
        if str(bin(n)).count('1')==1:
            return True
        else:
            return False