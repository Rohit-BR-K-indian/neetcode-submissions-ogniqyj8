# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root,arr):
            if root is None:
                arr.append(None)
                return
            
            arr.append(root.val)
            dfs(root.left,arr)
            dfs(root.right,arr)
        
        pArr = []
        dfs(p,pArr)
        qArr = []
        dfs(q,qArr)

        if len(qArr) > len(pArr) or len(pArr) > len(qArr):
            return False

        for x , y in zip(pArr,qArr):
            if x != y:
                return False

        return True