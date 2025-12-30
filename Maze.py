class Maze:
    def __init__(self, filename):
        self.grid = []
        self.height = 0
        self.width = 0
        self.load_map(filename)

    def load_map(self, filename):
        with open(filename,'r') as f:
            lines = f.read().splitlines()

        self.type = lines[0].split()[1]  # 'octile'
        self.height = int(lines[1].split()[1])
        self.width = int(lines[2].split()[1])
        
        # Read the actual map
        map_lines = lines[4:]  # everything after 'map' line
        self.grid = [list(line.strip()) for line in map_lines]

        # Additional Check
        if len(self.grid) != self.height or any(len(row) != self.width for row in self.grid):
            raise ValueError("Map size does not match height/width in header.")

    def display(self, start=None, goal=None, path=None):
        """Print the maze with optional start, goal, and path."""
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if start and (x, y) == start:
                    row += "S"
                elif goal and (x, y) == goal:
                    row += "E"
                elif path and (x, y) in path:
                    row += "*"
                else:
                    row += self.grid[y][x]
            print(row)

    def save_maze(self, filename, start=None, goal=None, path=None):
        """
        Save the maze to a file with optional start, goal, and path.
        start = (x, y)
        goal = (x, y)
        path = list of (x, y) tuples
        """
        with open(filename, "w") as f:
            # Write header (keeping the original format)
            f.write(f"type {self.type}\n")
            f.write(f"height {self.height}\n")
            f.write(f"width {self.width}\n")
            f.write("map\n")

            for y in range(self.height):
                row = ""
                for x in range(self.width):
                    if start and (x, y) == start:
                        row += "S"
                    elif goal and (x, y) == goal:
                        row += "E"
                    elif path and (x, y) in path:
                        row += "*"
                    else:
                        row += self.grid[y][x]
                f.write(row + "\n")  # write each row to the file


