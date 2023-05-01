class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bst(self, nums: list, start, end) -> TreeNode:
        if start > end:
            return None
        middle = (start + end) // 2
        result = TreeNode(nums[middle])
        result.left = self.bst(nums, start, middle - 1)
        result.right = self.bst(nums, middle + 1, end)
        return result

    def dfs(self, node: TreeNode) -> list:
        if node is None:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.dfs(root)
        return self.bst(nums, 0, len(nums) - 1)
