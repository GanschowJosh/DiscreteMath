from copy import deepcopy
class Tree:
    def __init__(self, size):
        if size < 2:
            print("Size of tree must be 2 or higher")
            return
        self.numNodes = size
        self.numEdges = size - 1
        self.matrix = [[0]*size for i in range(size)]
        self.workingMatrix = [[0]*size for i in range(size)]
    
    def addEdge(self, v, w):
        self.matrix[v-1][w-1] = 1
        self.matrix[w-1][v-1] = 1

    def printMatrix(self):
        print("    ", end="") #offset for labels
        for colLabel in range(1, self.numNodes+1):
            print(f"{colLabel:4}", end="")
        print()

        #print each row with a label
        for i in range(self.numNodes):
            print(f"{i + 1: 4}", end="") #row label
            for j in range(self.numNodes):
                print(f"{self.matrix[i][j]:4}", end="")
            print()
    
    #finding next leaf
    def findLeaf(self):
        for i in range(self.numNodes):
            count = 0
            for j in range(self.numNodes):
                if self.workingMatrix[i][j]:
                    count += 1
            if count == 1:
                return i
        return -1 #no leaf found

    #clearing all connections from a node, removing it from list
    def clearConnections(self, node):
        for i in range(self.numNodes):
            self.workingMatrix[node][i] = 0
            self.workingMatrix[i][node] = 0
            
    #generating prufer code
    def generatePrufer(self):
        self.workingMatrix = deepcopy(self.matrix)
        code = []
        while len(code) < self.numNodes - 2:
            nextLeaf = self.findLeaf()
            for j in range(len(self.workingMatrix[nextLeaf])):
                if self.workingMatrix[nextLeaf][j]:
                    code.append(j+1)
            self.clearConnections(nextLeaf)
        return code
                

    
            
#testing 
t = Tree(12)
t.printMatrix()
#adding edges
t.addEdge(1, 5)
t.addEdge(1, 8)
t.addEdge(1, 10)

t.addEdge(2, 7)
t.addEdge(2, 12)

t.addEdge(3, 8)

t.addEdge(4, 10)

t.addEdge(5, 12)
t.addEdge(5, 1)

t.addEdge(6, 12)

t.addEdge(7, 2)

t.addEdge(8, 3)
t.addEdge(8, 9)
t.addEdge(8, 1)

t.addEdge(9, 8)

t.addEdge(10, 4)
t.addEdge(10, 1)

t.addEdge(11, 12)

t.addEdge(12, 2)
t.addEdge(12, 5)
t.addEdge(12, 6)
t.addEdge(12, 11)

t.printMatrix()
code = t.generatePrufer()
print(code)
t.printMatrix()
