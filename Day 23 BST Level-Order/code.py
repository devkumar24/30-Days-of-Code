import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        level = 1
        
        def printlevel(root,level):
            if root is None:
                return False
            if level == 1:
                print(root.data,end = " ")
                return True
            left = printlevel(root.left, level - 1)
            right = printlevel(root.right, level - 1)
            return left or right
        
        while printlevel(root,level):
            level += 1
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
