# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthDFS(node, depth):
            if node == None:
                return depth
            
            return max(maxDepthDFS(node.left, depth + 1), maxDepthDFS(node.right, depth + 1))
        
        return maxDepthDFS(root, 0)
