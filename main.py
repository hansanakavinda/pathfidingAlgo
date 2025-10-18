import pygame
import random
from grid import grid, Start, End, gridsize, available_nods, numobstacles
from a_star import a_star
from visualization import draw_grid
from utils import success_criteria, cost_calculation

if __name__ == "__main__":
    pygame.init()
    cell_size = 50
    screen = pygame.display.set_mode((gridsize * cell_size, gridsize * cell_size + 50))
    clock = pygame.time.Clock()

    state = "initial"
    path = None
    visited_nodes = set()
    search_iterator = None
    current_path = None
    results_printed = False

    while True:
        if state == "initial":
            button_clicked, reset_clicked = draw_grid(screen, grid, gridsize, Start, End, state="initial")
            if button_clicked:
                state = "searching"
                search_iterator = a_star(search_mode=True)
                print("Searching")

        elif state == "searching":
            try:
                pos, current_path = next(search_iterator)
                visited_nodes.add(pos)
                draw_grid(screen, grid, gridsize, Start, End, state="searching", path=current_path, visited=visited_nodes)
                pygame.time.wait(300)  # 0.3-second delay for slower animation
                if pos == End:
                    path = current_path
                    state = "path"
                    print("Path found")
            except StopIteration:
                path = None
                state = "path"
                print("No path found")

        elif state == "path":
            button_clicked, reset_clicked = draw_grid(screen, grid, gridsize, Start, End, state="path", path=path)
            if reset_clicked:
                # Reset grid
                grid[:] = [[0 for _ in range(gridsize)] for _ in range(gridsize)]
                obstacle_nods = random.sample(available_nods, numobstacles)
                for r, c in obstacle_nods:
                    grid[r][c] = 1
                # Reset state
                state = "initial"
                path = None
                visited_nodes = set()
                search_iterator = None
                current_path = None
                results_printed = False

        pygame.display.flip()
        clock.tick(60)

        # Print results once in path state
        if state == "path" and not results_printed:
            if success_criteria(path):
                print("Valid path")
            else:
                print("\npath is not valid")
            visited_path =path
            print("Path :", visited_path)
            total_cost = cost_calculation(visited_path)
            print("Total Cost of the Path:", total_cost)
            results_printed = True