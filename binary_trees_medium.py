from collections import deque
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
    
    diameter = 0
    def height_for_diameter(self,root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.diameter = max(self.diameter, left+right)
        return 1+max(left,right)

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        self.height_for_diameter(root)
        return self.diameter
    
    import sys
    maxi = -sys.maxsize
    def max_sum_for_node(self,node):
        if node is None:
            return 0
        
        left = self.max_sum_for_node(node.left)
        right = self.max_sum_for_node(node.right)
        left = max(0,left)
        right = max(0,right)
        self.maxi = max(self.maxi, node.val+left+right)
        return node.val + max(left,right)

    
    def max_sum(self,root):
        self.max_sum_for_node(root)
        return self.maxi 
    
    def same_tree(self, p,q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.same_tree(p.left, q.left)
        right = self.same_tree(p.right, q.right)

        return left and right

    def zig_zag(self,root):
        result = []
        if root is None: 
            return result
        
        q = deque([root])
        flag = True

        while q:
            level_order = len(q)
            num_list = []
            while level_order:
                node = q.popleft()
                if flag:
                    num_list.append(node.val)
                else:
                    num_list.insert(0,node.val)
                if node.left: 
                    q.append(node.left) 
                if node.right: 
                    q.append(node.right)
                level_order-=1
            flag = not flag
            result.append(num_list)
        return result
    
    def left_boundary(self,node,res):
        while node is not None:
            leaf = node.left is None and node.right is None
            if not leaf:
                res.append(node.val)

            if node.left is not None:
                node = node.left
            else:
                node = node.right
            

    def right_boundary(self,node,res):
        temp = []
        while node is not None:
            leaf = node.left is None and node.right is None
            if not leaf:
                temp.append(node.val)

            if node.right is not None:
                node = node.right
            else:
                node = node.left
        
        temp.reverse()
        res.extend(temp)

    def leaves(self,node,leaf):
        if node is None:
            return
        last_node = node.left is None and node.right is None
        if last_node:
            leaf.append(node.val)
            return
        self.leaves(node.left, leaf)
        self.leaves(node.right,leaf)

    def boundary_traversal(self,root,res):
        if root is None:
            return res
        is_leaf = (root.left is None and root.right is None)
        if not is_leaf:
            res.append(root.val)
        self.left_boundary(root.left,res)
        self.leaves(root,res)
        self.right_boundary(root.right,res)

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

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    sol = Solution()
    print("Height of tree:", sol.height_of_tree(root))
    print("Is balanced or not:", sol.isBalanced(root))
    # print("Diameter:", sol.diameterOfBinaryTree(root))
    print("Max sum in tree:", sol.max_sum(root))
    print("Are trees same:", sol.same_tree(root, root2))
    print("Zig-Zag Traversal:", sol.zig_zag(root))
    print("Boundary:", sol.boundary_traversal(root,[]))
 