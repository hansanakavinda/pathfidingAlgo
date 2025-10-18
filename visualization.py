import pygame

def draw_grid(screen, grid, gridsize, start, end, state="initial", path=None, visited=None):
    
    cell_size = 50
    screen_width = gridsize * cell_size

    WHITE = (255, 255, 255)  
    BLACK = (0, 0, 0)      
    GREEN = (0, 255, 0)     
    RED = (255, 0, 0)      
    YELLOW = (255, 255, 0)  
    BLUE = (0, 0, 255)      
    GRAY = (200, 200, 200)  

    # Button properties
    button_rect = pygame.Rect(50, gridsize * cell_size + 10, screen_width - 100, 30)
    reset_rect = pygame.Rect(50, gridsize * cell_size + 10, screen_width - 100, 30)
    font = pygame.font.SysFont(None, 24)
    button_text = font.render("Start Search", True, BLACK)
    reset_text = font.render("Reset", True, BLACK)

    path_set = set(path) if path else set()
    visited_set = set(visited) if visited else set()
    button_clicked = False
    reset_clicked = False

    # Draw the grid
    screen.fill(WHITE)
    for i in range(gridsize):
        for j in range(gridsize):
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            if (i, j) == start:
                pygame.draw.rect(screen, BLACK, rect)
            elif (i, j) == end:
                pygame.draw.rect(screen, GREEN, rect)
            elif (i, j) in path_set and (i, j) not in (start, end) and state in ("searching", "path"):
                pygame.draw.rect(screen, BLUE, rect)
            elif (i, j) in visited_set and state == "searching" and (i, j) not in (start, end):
                pygame.draw.rect(screen, YELLOW, rect)
            elif grid[i][j] == 1:
                pygame.draw.rect(screen, RED, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Grid lines

    # Draw buttons based on state
    if state == "initial":
        pygame.draw.rect(screen, GRAY, button_rect)
        screen.blit(button_text, (button_rect.x + 20, button_rect.y + 5))
    elif state == "path":
        pygame.draw.rect(screen, GRAY, reset_rect)
        screen.blit(reset_text, (reset_rect.x + 20, reset_rect.y + 5))

    # Check for button clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "initial" and button_rect.collidepoint(event.pos):
                button_clicked = True
            elif state == "path" and reset_rect.collidepoint(event.pos):
                reset_clicked = True

    return button_clicked, reset_clicked