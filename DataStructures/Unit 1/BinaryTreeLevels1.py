class Node:
    # Constructor with 3 elements: value, left child and right child
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    # To print the node, only it's value is printed
    def __str__(self):
        return str(self.value)
# Function to print by levels
def traverse(root):
    current_level = [root] # List of current levels to be checked, starts with the root
    while current_level: # Go through every current level
        print(' '.join(str(node) for node in current_level)) # Print each node in the level with spaces inbetween
        next_level = [] # New list to save next nodes to go through
        for n in current_level: # Check for children of each node in the current level
            if n.left: 
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right) # Add children to the next level list
        current_level = next_level # Replace current level with next level
# Building tree
t = Node(8, Node(3, Node(1), Node(6)), Node(10, Node(14)))


traverse(t)