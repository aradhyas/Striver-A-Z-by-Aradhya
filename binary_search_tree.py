# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        
        if root.val>val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
    
    def floorInBST(self, root, x):
        floor_val = None
        curr = root

        while curr:
            if curr.val == x:
                return curr.val
            elif curr.val > x:
                curr = curr.left
            else:
                floor_val = curr.val   # possible floor
                curr = curr.right

        return floor_val
    
    def insertIntoBST(self, root, val):
        if root is None:
            return val

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
    def deleteBST(self, root, key):
        if root is None:
            return key
        
        temp = root
        if key < root.val:
               root.left = self.deleteBST(root.left, key) 
        elif key > root.val:
               root.right = self.deleteBST(root.right, key) 
        else:
            if not root.left and not root.right:
                return None
            
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: Found the node to delete
            # Case A: No child
            if not root.left and not root.right:
                return None

            # Case B: One child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case C: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node

    def kthSmallest(self, root, k):
        self.count = 0
        self.result = None
        self.k = k
        self.inorder(root)
        return self.result

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.count+=1
        if self.count == self.k:
            self.result = root.val
            return
        self.inorder(root.right)

    def kthLargest(self, root, k):
        self.count = 0
        self.result = None
        self.k = k
        self.revInorder(root)
        return self.result

    def revInorder(self, root):
        if root is None or self.result is not None:
            return
        self.revInorder(root.right)
        self.count += 1
        if self.count == self.k:
            self.result = root.val
            return
        self.revInorder(root.left)

    def isValidBST(self, root):
        self.prev = None
        def inorder(self,node):
            if node is None:
                return None
            
            if not inorder(node.left):
                return False
            
            if self.prev is not None and self.prev>=node.val:
                return False
            self.prev = node.val

            return self.inorder(node.right)
        return inorder(root)

    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        return left if left else right

    def bstFromPreorder(self, preorder):
        self.i = 0
        def build(low,high):
            if self.i == len(preorder):
                return None
            x = preorder[self.i]
            if not (low < x < high):
                return None

            self.i += 1
            node = TreeNode(x)
            node.left = build(low,node.val)
            node.right = build(node.val,high)

            return node
        
        return build(-inf, inf)

    def inorderPredecessorSuccessor(self, root, key):
        pred = None
        succ = None

        curr = root
        while curr:
            if curr.val<key:
                pred = curr.val
                curr = curr.right
            else:
                curr = curr.left
        
        curr = root
        while curr:
            if curr.val>key:
                succ = curr.val
                curr = curr.left
            else:
                curr = curr.right
        
        return pred,succ

    def find_pair(self, root, k):
        seen = set()

        def dfs(node):
            if not node:
                return False
            
            need = k - node.val
            if need in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
     

# Build the BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()

# Search for a value
val = 2
result = sol.searchBST(root, val)

# Search
val = 2
node = sol.searchBST(root, val)
print(f"Search {val}:", node.val if node else "Not found")

# Floor
x = 5
print(f"Floor of {x}:", sol.floorInBST(root, x))

# Insert
root = sol.insertIntoBST(root, 5)
print("After inserting 5:")
print()

# Delete
root = sol.deleteNode(root, 2)
print("After deleting 2:")
print()

# kth smallest
k = 3
print(f"{k}th smallest:", sol.kthSmallest(root, k))
