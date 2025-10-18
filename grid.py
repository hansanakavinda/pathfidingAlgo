import random

gridsize = 7
Start = (0, 0)
End = (2, 4)
numobstacles = 10

#grid filled with zeros
grid = [[0 for _ in range(gridsize)] for _ in range(gridsize)]

# list of all nodes without start and goal
available_nods = [(r, c) for r in range(gridsize) for c in range(gridsize)
                       if (r, c) != Start and (r, c) != End]

#randomly place obstacles
obstacle_nods = random.sample(available_nods, numobstacles)

# mark chosen obstacles on grid
for r, c in obstacle_nods:
    grid[r][c] = 1