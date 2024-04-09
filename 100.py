class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q:TreeNode) -> bool:
        pq = self.go(p)
        qq = self.go(q)
        return pq==qq
    def go(self,node):
        qur = []
        if node is not None:
            qur.append(node.val)
            qur += self.go(node.left)
            qur += self.go(node.right)
        else:
            qur.append(None)
            return qur
        return qur
    
# ac