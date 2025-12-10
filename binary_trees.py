from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

        traverse(root)
        return res
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node):
            if node is None:
                return
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)

        traverse(root)
        return res
    
    def bfs(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            node = q.popleft()
            result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return result
    
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr is not None or stack:
            # Go as left as possible
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # Process node
            curr = stack.pop()
            res.append(curr.val)

            # Go to right subtree
            curr = curr.right

        return res
    
    def preorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            # push right first so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
    
    def postorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack1 = [root]
        stack2 = []
        res = []

        # First phase: modified preorder (Root, Right, Left)
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        # Second phase: reverse order → Left, Right, Root
        while stack2:
            node = stack2.pop()
            res.append(node.val)

        return res


if __name__ == "__main__":
# Building this tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()

    print("DFS Preorder:  ", sol.preorderTraversal(root))     # [1, 2, 4, 5, 3]
    print("DFS Inorder:   ", sol.inorderTraversal(root))      # [4, 2, 5, 1, 3]
    print("DFS Postorder: ", sol.postorderTraversal(root))    # [4, 5, 2, 3, 1]
    print("BFS LevelOrder:", sol.bfs(root))          # [1, 2, 3, 4, 5]
    print("Iter Preorder:  ", sol.preorderTraversal_iterative(root))
    print("Iter Inorder:   ", sol.inorderTraversal_iterative(root))
    print("Iter Postorder: ", sol.postorderTraversal_iterative(root))
