class Graph:

	#def __init__(self,vertices):
	#	self.V = vertices   #Number of vertices
	#	self.graph = [[0]*self.V for x in range(self.V)] # Create 2d Matrix of V * V
	#	self.visited = [False]*self.V #Create boolean list of visited vertices

	def __init__(self,vertices):
		self.V = vertices
		self.graph = [None]*self.V # Create List of  V
		for i in range(self.V):
			self.graph[i] = list() # Create List for Each vertices to store adj nodes
		self.visited = [False]*self.V #Create boolean list of visited vertice


	def add_edge(self,i,j):
		self.graph[i].append(j)
        #for Unidirection Array
        #self.graph[j][i] = cost

	#get nearby not visited nodes
	def getNodes(self,node):
		nodes = []
		for i in range(self.V):
			if self.graph[node][i] == 1 and self.visited[i] == False: #return only vertices which are not visited
				nodes.append(i)
		return nodes

	def BFS(self,start):
		queue = []
		queue.append(start)
		self.visited[start] = True
		while queue:
			start = queue.pop(0)
			print(start)
			for i in self.graph[start]:
				if self.visited[i] == False:
					queue.append(i)
					self.visited[i] = True
	def DFS(self,start):
		queue = []
		queue.append(start)
		self.visited[start] = True
		while queue:
			start = queue.pop()
			print(start)
			for i in self.graph[start]:
				if self.visited[i] == False:
					queue.append(i)
					self.visited[i] = True


	def print_graph(self):
		print(self.graph)


if __name__ == '__main__':
	V = 5
	graph = Graph(V)

#    graph.print_graph()

	graph.add_edge(0,1)
	graph.add_edge(0,2)
	graph.add_edge(1,2)
	graph.add_edge(2,0)
	graph.add_edge(2,3)
	graph.add_edge(3,3)

	graph.print_graph()

	graph.DFS(2)

	#graph.getNodes(0)
