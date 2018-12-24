# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    visited = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.visited = []
        if root:
            self.visit(root)
        return self.visited

    def visit(self, node):
        if (node.left):
            self.visit(node.left)
        if (node.right):
            self.visit(node.right)
        self.visited.append(node.val)