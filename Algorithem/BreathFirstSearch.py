from Queue import FIFO

class Node:
    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent
        

class BFS:
    def __init__(self, maze):
        self.maze = maze

    def find_neighbours(self, x, y):
        """Return walkable neighbors in 4 directions."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.maze.is_free(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def solve(self, start, goal):
        """
        BFS algorithm to find shortest path from start to goal.
        Returns path as a list of (x, y) tuples or None if no path.
        """
        queue = FIFO()
        start_node = Node(start)
        queue.enqueue(start_node)

        visited = set()
        visited.add(start)

        while not queue.is_empty():
            current_node = queue.dequeue()
            x, y = current_node.point


            if current_node.point == goal:
                path = []
                node = current_node
                while node is not None:
                    path.append(node.point)
                    node = node.parent
                path.reverse()
                return path, visited
            
            for nx, ny in self.find_neighbours(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    neighbor_node = Node((nx, ny), current_node)
                    queue.enqueue(neighbor_node)

        return None
