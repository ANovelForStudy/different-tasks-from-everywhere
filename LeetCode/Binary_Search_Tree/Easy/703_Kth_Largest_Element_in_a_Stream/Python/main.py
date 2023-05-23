
from typing import List


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.insert(self.root, num)

    def insert(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        root.count += 1
        return root

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        kth_node = self.kth_node(self.root, self.k)
        return kth_node.val

    def kth_node(self, root: TreeNode, k: int) -> TreeNode:
        if not root:
            return None
        right_count = root.right.count if root.right else 0
        if k <= right_count:
            return self.kth_node(root.right, k)
        elif k == right_count + 1:
            return root
        else:
            return self.kth_node(root.left, k - right_count - 1)
