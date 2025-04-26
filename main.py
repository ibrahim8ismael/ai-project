import pygame 
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_RED = (139, 0, 0)

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.original_color = color
        self.is_hovered = False

    def draw(self, surface):
        color = LIGHT_GRAY if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=12)
        
        font = pygame.font.SysFont('comicsans', 40)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

def draw_menu():
    WIN.fill(BLACK)
    # Draw title
    font = pygame.font.SysFont('comicsans', 80)
    title = font.render('Checkers Game', True, RED)
    WIN.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4))
    
    # Create and draw buttons
    button_width = 200
    button_height = 60
    two_player_btn = Button(
        WIDTH//2 - button_width//2,
        HEIGHT//2,
        button_width,
        button_height,
        '2 Players',
        DARK_RED
    )
    ai_player_btn = Button(
        WIDTH//2 - button_width//2,
        HEIGHT//2 + 100,
        button_width,
        button_height,
        'vs AI',
        DARK_RED
    )
    
    two_player_btn.draw(WIN)
    ai_player_btn.draw(WIN)
    
    pygame.display.update()
    return two_player_btn, ai_player_btn

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def menu():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    game_mode = None
    
    two_player_btn, ai_player_btn = draw_menu()
    
    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        
        # Handle button hover effects
        two_player_hover = two_player_btn.handle_event(mouse_pos)
        ai_player_hover = ai_player_btn.handle_event(mouse_pos)
        
        if two_player_hover or ai_player_hover:
            draw_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return None
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if two_player_btn.rect.collidepoint(mouse_pos):
                    game_mode = "2P"
                    run = False
                elif ai_player_btn.rect.collidepoint(mouse_pos):
                    game_mode = "AI"
                    run = False
    
    return game_mode

def main(game_mode):
    run = True
    clock = pygame.time.Clock() 
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.winner() is not None:
            print(f"Winner: {'RED' if game.winner() == (255, 0, 0) else 'WHITE'}")
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()
        
    pygame.quit()

if __name__ == "__main__":
    game_mode = menu()
    if game_mode:
        main(game_mode)