class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, root.val)]  # (current node, max value so far)

        while stack:
            node, maxVal = stack.pop()

            if node.val >= maxVal:
                count += 1

            # Update maxVal for children
            newMax = max(maxVal, node.val)

            if node.left:
                stack.append((node.left, newMax))
            if node.right:
                stack.append((node.right, newMax))

        return count
