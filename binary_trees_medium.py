class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height_of_tree(self,root):
        if root is None:
            return 0
        
        left_h = self.height_of_tree(root.left)
        right_h = self.height_of_tree(root.right)
        return 1+max(left_h,right_h)
    
    def isBalanced(self, root):
        # helper returns:
        # - height of subtree if balanced
        # - -1 if subtree is NOT balanced
        def check(node) -> int:
            if node is None:
                return 0  # empty tree has height 0 and is balanced

            left = check(node.left)
            if left == -1:
                return -1  # left subtree already unbalanced

            right = check(node.right)
            if right == -1:
                return -1  # right subtree already unbalanced

            # if current node is unbalanced
            if abs(left - right) > 1:
                return -1

            # return height of this subtree
            return 1 + max(left, right)

        # tree is balanced if helper did NOT return -1
        return check(root) != -1
    

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
    print("Height of tree:", sol.height_of_tree(root))
    print("Is balanced or not:", sol.isBalanced(root))
 