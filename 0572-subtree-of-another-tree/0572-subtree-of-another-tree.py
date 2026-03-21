# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root==None):
            return False

        if self.isIdentical(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    
    def isIdentical(self,s,t):
        if  s == None and t == None:
            return True

        if  s == None or t == None:
            return False
        
        if  s.val != t.val:
            return False

        return self.isIdentical(s.left,t.left) and self.isIdentical(s.right,t.right)