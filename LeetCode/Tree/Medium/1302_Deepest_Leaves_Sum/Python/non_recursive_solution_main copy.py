
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:

        nodes = [root]
        current_node = 0

        while len(nodes):

            current_level_count, deepest_leaves_sum = len(nodes), 0

            for _ in range(current_level_count):

                current_node = nodes.pop(0)
                deepest_leaves_sum += current_node.val

                if current_node.left:
                    nodes.append(current_node.left)
                if current_node.right:
                    nodes.append(current_node.right)

        return deepest_leaves_sum
