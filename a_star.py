import heapq
from grid import grid, Start, End, gridsize

# Directions: Right, Down, Left, Up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def a_star(search_mode=False):
    queue = [(0, 0, Start, [Start])]  # (f_score, g_score, position, path)
    heapq.heapify(queue)
    
    visited = set()
    visited.add(Start)
    s = 0
    while queue:
        s += 1
        f_score, g_score, (x, y), path = heapq.heappop(queue)
        print("Selected F_score:", f_score)

        if search_mode:
            yield ((x, y), path) #for visualization

        if (x, y) == End:
            if not search_mode:
                return path
            return path
        i = 0 
        for dx, dy in DIRECTIONS:
            i += 1
            nx, ny = x + dx, y + dy
            if 0 <= nx < gridsize and 0 <= ny < gridsize and grid[nx][ny] == 0:
                if (nx, ny) not in visited:
                    new_g_score = g_score + 1
                    h_score = manhattan_distance((nx, ny), End)
                    f_score = new_g_score + h_score
                    print("New F_score:", f_score)
                    new_path = path + [(nx, ny)]
                    heapq.heappush(queue, (f_score, new_g_score, (nx, ny), new_path))
                    visited.add((nx, ny))

    if not search_mode:
        return None
    return None

if __name__ == "__main__":
    path = a_star()
    if path:
        print("Shortest Path Found:", path)
    else:
        print("No path found")