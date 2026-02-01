# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.depth(root.right, 0), self.depth(root.left, 0))
    def depth(self, node: Optional[TreeNode], count)  -> int:
        if node == None:
            return count + 1
        else:
            count += 1
            return max(self.depth(node.right, count), self.depth(node.left, count))