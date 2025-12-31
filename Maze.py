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
        
    def is_free(self, x, y):
        """Return True if (x, y) is inside the maze and not a wall."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == '.'
        return False

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

    def save_as_ppm(self, filename, start=None, goal=None, path=None, visited=None):
        scale = 2  # enlarge pixels
        with open(filename, "w") as f:
            f.write("P3\n")
            f.write(f"{self.width * scale} {self.height * scale}\n")
            f.write("255\n")

            for y in range(self.height):
                for sy in range(scale):
                    for x in range(self.width):
                        for sx in range(scale):
                            if start and (x, y) == start:
                                color = (0, 255, 0)       # green
                            elif goal and (x, y) == goal:
                                color = (255, 0, 0)       # red
                            elif path and (x, y) in path:
                                color = (0, 0, 255)       # blue
                            elif self.grid[y][x] == '@':
                                color = (0, 0, 0)         # black
                            elif visited and (x, y) in visited:
                                color = (200, 200, 200)
                            else:
                                color = (255, 255, 255)   # white

                            f.write(f"{color[0]} {color[1]} {color[2]} ")
                    f.write("\n")
