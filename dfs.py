# depth first search algorithm
'''
Step 1: Create a set or array to keep track of visited nodes.
Step 2: Choose a starting node.
Step 3: Create an empty stack and push the starting node onto the stack.
Step 4: Mark the starting node as visited.
Step 5: While the stack is not empty, do the following:
    Pop a node from the stack.
    Process or perform any necessary operations on the popped node.
    Get all the adjacent neighbors of the popped node.
    For each adjacent neighbor, if it has not been visited, do the following:
        Mark the neighbor as visited.
        Push the neighbor onto the stack.
Step 6: Repeat step 5 until the stack is empty.'''

# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

# Driver's code


# Create a graph given
# in the above diagram
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is DFS from (starting from vertex 2)")
	# Function call
	g.DFS(2)

# This code is contributed by Neelam Yadav
