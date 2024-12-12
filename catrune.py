import pygame
import time

# --- Constants ---
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
TILE_SIZE = 32
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
BAR_WIDTH = 200
BAR_HEIGHT = 15
BAR_X = 10
BAR_Y = SCREEN_HEIGHT - BAR_HEIGHT - 10
HP_COLOR = (255, 0, 0)
MP_COLOR = (0, 255, 255)

# --- Game Variables ---
game_state = "main_menu"  # Initial state
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Sample HP/MP values (these will be dynamic in a more complete game)
max_hp = 100
current_hp = 75
max_mp = 50
current_mp = 25

# --- Map Data ---
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Deltarune-ish")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)

# --- Functions ---

def draw_main_menu():
    title_text = font.render("DELTARUNE-ISH", True, WHITE)
    start_text = font.render("Press Enter to Start", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)

def draw_map():
    for row_index, row in enumerate(map_data):
        for col_index, tile in enumerate(row):
            tile_x = col_index * TILE_SIZE
            tile_y = row_index * TILE_SIZE
            if tile == 0:
                color = GREEN  # Grass
            elif tile == 1:
                color = GRAY  # Boundary
            pygame.draw.rect(screen, color, (tile_x, tile_y, TILE_SIZE, TILE_SIZE))

def draw_hp_mana_bar():
    hp_percentage = current_hp / max_hp
    mp_percentage = current_mp / max_mp
    hp_width = BAR_WIDTH * hp_percentage
    mp_width = BAR_WIDTH * mp_percentage

    pygame.draw.rect(screen, GRAY, (BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT))  # Border
    pygame.draw.rect(screen, HP_COLOR, (BAR_X, BAR_Y, hp_width, BAR_HEIGHT))  # HP
    pygame.draw.rect(screen, MP_COLOR, (BAR_X, BAR_Y + 5, mp_width, BAR_HEIGHT / 2))  # MP

    hp_text = font.render(f"HP: {current_hp}/{max_hp}", True, WHITE)
    mp_text = font.render(f"MP: {current_mp}/{max_mp}", True, WHITE)
    
    screen.blit(hp_text, (BAR_X + BAR_WIDTH + 5, BAR_Y))
    screen.blit(mp_text, (BAR_X + BAR_WIDTH + 5, BAR_Y + 10))

def draw_gameplay():
    draw_map()
    # Draw player (a simple rectangle for now)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, TILE_SIZE, TILE_SIZE))
    draw_hp_mana_bar()


def handle_input():
    global game_state, player_x, player_y, current_hp, current_mp  # Add hp/mp
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if game_state == "main_menu" and event.key == pygame.K_RETURN:
                game_state = "gameplay"
            elif game_state == "gameplay":
                new_player_x = player_x
                new_player_y = player_y
                if event.key == pygame.K_LEFT:
                    new_player_x -= TILE_SIZE
                elif event.key == pygame.K_RIGHT:
                    new_player_x += TILE_SIZE
                elif event.key == pygame.K_UP:
                    new_player_y -= TILE_SIZE
                elif event.key == pygame.K_DOWN:
                    new_player_y += TILE_SIZE
                # Check for collision with boundaries
                if not check_collision(new_player_x, new_player_y):
                    player_x = new_player_x
                    player_y = new_player_y
                    current_hp -= 1 if current_hp > 0 else 0 # Example decrement
                    current_mp += 1 if current_mp < max_mp else 0 # Example increment


def check_collision(x, y):
    # Basic tile-based collision detection
    row = y // TILE_SIZE
    col = x // TILE_SIZE
    if row < 0 or row >= len(map_data) or col < 0 or col >= len(map_data[0]):
         return True # Out of bounds collision
    if map_data[row][col] == 1:
        return True  # Collision
    else:
        return False

# --- Game Loop ---
running = True
while running:
    start_time = time.time()

    handle_input()

    screen.fill(BLACK)  # Clear screen

    if game_state == "main_menu":
        draw_main_menu()
    elif game_state == "gameplay":
        draw_gameplay()

    pygame.display.flip()

    elapsed_time = time.time() - start_time
    target_delay = 1 / 60.0 - elapsed_time
    if target_delay > 0:
        time.sleep(target_delay)

    clock.tick(60)  # Limit to 60 frames per second
