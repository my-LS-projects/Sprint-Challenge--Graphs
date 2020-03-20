"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("ERROR: Vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("ERROR: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("ERROR: Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        queue = Queue()
        # Enqueue starting vertex
        queue.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # DQ first vertex
            current = queue.dequeue()
            # Check if visited
            if current not in visited:
                # If not...
                print(current)
                # Mark as visited
                visited.add(current)
                # ENQ neighbors
                for neighbor in self.get_neighbors(current):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create Stack (LIFO)
        stack = Stack()
        # Add starting vertex
        stack.push(starting_vertex)
        # Create empty set
        visited = set()
        while stack.size() > 0:
            # Pop off first vertex
            current = stack.pop()
            # If vertex has not been visited...
            if current not in visited:
                print(current)
                # Add to visited
                visited.add(current)
                # Add neighbors to the stack
                for neighbor in self.get_neighbors(current):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        Will go row by row.
        Everything that's one away, then two away, then three, etc
        """
        # Create a queue
        queue = Queue()
        # ENQ PATH to starting vertex
        queue.enqueue([starting_vertex])
        # create set to store visited vertices
        visited = set()
        # while queue is not empty...
        while queue.size() > 0:
            # DQ first PATH
            path = queue.dequeue()
            # GRAB VERTEX FROM END OF PATH
            last = path[-1]
            # Check if visited...
            # If not...
            if last not in visited:
                # Mark as visited and
                visited.add(last)
                # CHECK IF IT IS TARGET
                if last == destination_vertex:
                    return path
                # ENQ PATH to all neighbors by
                for neighbor in self.get_neighbors(last):
                    # MAKING COPY TO PATH
                    copy = path.copy()
                    copy.append(neighbor)
                    # ENQ COPY
                    queue.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            last = path[-1]

            if last not in visited:
                visited.add(last)
                if last == destination_vertex:
                    return path
                for neighbor in self.get_neighbors(last):
                    copy = path.copy()
                    copy.append(neighbor)
                    stack.push(copy)

    def dfs_recursive(
        self, starting_vertex, destination_vertex, visited=None, path=None
    ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            copy = path.copy()
            copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, copy
                )
                if new_path is not None:
                    return new_path
        return None


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
