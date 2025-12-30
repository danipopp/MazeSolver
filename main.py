from Maze import Maze

maze = Maze('maze-map/maze512-1-0.map')

start = (317, 343)
end = (309, 336)

maze.save_maze('solve.map', start, end)