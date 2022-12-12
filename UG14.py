class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set()

    def vertex(self): #mencetak seluruh vertex
        print("\nSeluruh Node = ", end = "")
        for key, value in self._data.items():
            print(key, end=" ")
        print()
    
    def edge(self): #mencetak seluruh edge
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)

        print("Seluruh Edge = ", end = "")
        for item in listEdge:
            print(item, end = ' ')
        print()

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    def bfs(self, node):
        print("Traversing BFS = ",end= " ")
        visited = []
        visited.append(node)
        queue = []
        queue.append(node)

        while queue:
            node = queue.pop(0)
            print ( node, end = " " )
            for item in self._data[node]:
                if item not in visited:
                    visited.append(item)
                    queue.append(item)

# silahkan buat graph seperti pada soal
graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b','c')
graph.addEdge('b', 'd')
graph.addEdge('d', 'e')
graph.addEdge('e', 'f')
graph.addEdge('c', 'g')
graph.addEdge('c', 'e')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs('a')