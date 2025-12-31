from Maze import Maze
from Algorithem.BreathFirstSearch import BFS

maze = Maze('maze-map/maze512-1-0.map')

_bfs = BFS(maze)

start = (2, 449)
end = (133, 509)

path, visited = _bfs.solve(start, end)

maze.save_maze('solve.map', start, end, path)
maze.save_as_ppm('solution.ppm', start, end, path, visited)