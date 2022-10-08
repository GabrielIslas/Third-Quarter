class Node:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def addNeighbor(self, neighbor, weight = 0):
        self.connections[neighbor] = weight

    def getConnections(self):
        return self.connections.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connections[neighbor]

    def __str__(self):
        return str(self.id) + " conectado con " + str(([x.getId() for x in self.getConnections()])) + " con peso " + str(([self.getWeight(x) for x in self.getConnections()]))

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.addNeighbor(node2, 4)
node1.addNeighbor(node4, 2)
node2.addNeighbor(node4, 1)
node2.addNeighbor(node3, 1)
print(node1)
print(node2)