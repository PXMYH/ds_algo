#!/usr/bin/python3

class TreeNode:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None
    
    def print(self):
        print(f"{self.root}")
        print(f"{self.left}")
        print(f"{self.right}")
    
root_node = TreeNode("CEO")
root_node.print()