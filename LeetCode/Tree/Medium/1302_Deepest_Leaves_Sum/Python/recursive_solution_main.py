
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        result = []

        def func(node: Optional[TreeNode], level):

            if level == len(result):
                result.append(node.val)
            else:
                result[level] += node.val

            if node.left:
                func(node.left, level+1)
            if node.right:
                func(node.right, level+1)

        func(root, 0)
        return result[-1]
