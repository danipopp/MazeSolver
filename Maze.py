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

        lines = lines

    def display(self):
        pass


