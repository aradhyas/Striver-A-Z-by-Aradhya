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