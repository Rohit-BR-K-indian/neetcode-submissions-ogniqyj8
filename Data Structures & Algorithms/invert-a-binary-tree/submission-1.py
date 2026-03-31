# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)

        while q:
            t = q.popleft()
            if t:
                t.left , t.right = t.right , t.left
                q.append(t.left)
                q.append(t.right)
        
        return root
        
        