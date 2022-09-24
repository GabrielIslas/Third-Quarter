# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:55:11 2022

@author: gabri
"""

class BinaryTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
    def __str__(self):
        printString = f"Node {self.value}"
        if self.leftChild is not None:
            printString += f", Left child {self.leftChild.value}"
        if self.rightChild is not None:
            printString += f", Right child {self.rightChild.value}"
        if self.leftChild is None and self.rightChild is None:
            printString += ", No children"
        printString += "\n"
        if self.leftChild is not None:
            printString += self.leftChild.__str__()
        if self.rightChild is not None:
            printString += self.rightChild.__str__()
        return printString
        
    def insertLeft(self, node):
        if self.leftChild is not None:
            node.leftChild = self.leftChild
        self.leftChild = node
        
    def insertRight(self, node):
        if self.rightChild is not None:
            node.rightChild = self.rightChild
        self.rightChild = node
        
    def sumar(value1, value2):
        return value1 + value2
    
    
        
    
print(BinaryTreeNode.sumar(2, 5))

node = BinaryTreeNode("A")
nodeB = BinaryTreeNode("B")
nodeC = BinaryTreeNode("C")
node.insertLeft(nodeB)
node.insertRight(nodeC)
print(node)
            