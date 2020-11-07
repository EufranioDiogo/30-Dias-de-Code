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
        from collections import deque

        queue = deque()
        node = root
        
        if node:
            queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()

            print(node.data, end=' ')

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        #Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)