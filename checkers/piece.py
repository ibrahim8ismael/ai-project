import pygame
from .constants import RED, WHITE, SQUARE_SIZE, BLACK

class Piece:
    PADDING = 15
    OUTLINE = 2
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()
        
    def calc_pos(self):
        """Calculate the pixel position based on row and column"""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        """Promote piece to king"""
        self.king = True
    
    def draw(self, win):
        """Draw the piece on the window"""
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            # Draw a crown or some indication that this is a king
            # For now, we'll just draw a smaller circle in the middle
            pygame.draw.circle(win, BLACK if self.color == WHITE else WHITE, 
                              (self.x, self.y), radius // 2)
    
    def move(self, row, col):
        """Move piece to a new position"""
        self.row = row
        self.col = col
        self.calc_pos()