class BinaryTreeNode:
    # Constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert element on the left
    def leftInsert(self, newLeft):
        leftNode = BinaryTreeNode(newLeft)
        if self.left != None:
            leftNode.left = self.left
        self.left = leftNode
    # Insert element on the right
    def rightInsert(self, newRight):
        rightNode = BinaryTreeNode(newRight)
        if self.right != None:
            rightNode.right = self.right
        self.right = rightNode
    # Creates the list with levels of each node
    def nodeLevels(self, level = 0, nodelevelList = []):
        nodelevelList.append([self.value, level])
        if self.left != None:
            self.left.nodeLevelIndividual(level + 1, nodelevelList)
        if self.right is not None:
            self.right.nodeLevelIndividual(level + 1, nodelevelList)
        return nodelevelList
    # Secondary function to modify the level list
    def nodeLevelIndividual(self, level = 0, nodelevelList = []):
        nodelevelList.append([self.value, level])
        if self.left != None:
            self.left.nodeLevelIndividual(level + 1, nodelevelList)
        if self.right != None:
            self.right.nodeLevelIndividual(level + 1, nodelevelList)
    # Checks the level list and prints it like the exercise asks
    def printByLevels(self):
        nodeLevelList = self.nodeLevels()
        nodesByLevels = []
        for node in nodeLevelList:
            if len(nodesByLevels) < node[1] + 1:
                nodesByLevels.append([])
            nodesByLevels[node[1]].append(node[0])
        for nodelevel in nodesByLevels:
            print(nodelevel)
# Building tree
root = BinaryTreeNode(8)
root.leftInsert(3)
root.rightInsert(10)
root.left.leftInsert(1)
root.left.rightInsert(6)
root.right.rightInsert(14)
root.left.right.leftInsert(4)
root.left.right.rightInsert(7)
root.right.right.leftInsert(13)
# Print level organization
root.printByLevels()