from collections import defaultdict


class Graph:
    def __init__(self, n):
        # Initialize a dict of list
        # {0: [], 1: [], 2: []}
        self.graph = defaultdict(lambda: [] * n)
        print('hm', self.graph)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        # Mark current node as visited and print it
        visited.add(v)
        # print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):
        visited = set()

        # Call the recursive helper function to print DFS Traversal
        self.DFSUtil(v, visited)

    def BFS(self, s):
        # Mark all vertices as not visited
        visited = [False] * len(self.graph)
        print(visited)
        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeues vertex s.
            # If adjacent has not been visited,
            # mark it as visited and enqueue it
            for neighbor in self.graph[s]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# t = int(input())
# for i in range(t):
#     n,m = [int(value) for value in input().split()]
#     graph = Graph(n)
#     for i in range(m):
#         x,y = [int(x) for x in input().split()]
#         graph.connect(x-1,y-1)
#     s = int(input())
#     graph.find_all_distances(s-1)


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.graph)
    g.BFS(2)
