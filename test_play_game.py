import unittest
import pygame
from large_board_tic_tac_toe import RandomBoardTicTacToe  # Import your main class

class TestPlayGame(unittest.TestCase):
    
    def setUp(self):
        """ Set up a game instance before each test. """
        self.game = RandomBoardTicTacToe()
        self.game.board = [[""] * self.game.GRID_SIZE for _ in range(self.game.GRID_SIZE)]

    def test_quit_event(self):
        """ Test if the game loop exits on QUIT event. """
        quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(quit_event)

        # Ensure the game loop runs with the quit event
        self.game.play_game()

        # Check if the event queue is empty (i.e., game should quit)
        self.assertFalse(any(event.type == pygame.QUIT for event in pygame.event.get()))

    def test_mouse_click_on_empty_cell(self):
        """ Test if clicking an empty cell places 'X' and updates the board. """
        x, y = self.game.WIDTH // 2, self.game.HEIGHT // 2  # Click in the center of a cell
        col = int(x // (self.game.WIDTH + self.game.MARGIN))
        row = int(y // (self.game.HEIGHT + self.game.MARGIN))

        mouse_event = pygame.event.Event(pygame.MOUSEBUTTONUP, {"pos": (x, y)})
        pygame.event.post(mouse_event)

        self.game.play_game()  # Run the function

        self.assertEqual(self.game.board[row][col], "X")  # Ensure 'X' is placed

    def test_board_boundaries(self):
        """ Test clicking outside the board does not modify the board. """
        x, y = self.game.WIDTH * self.game.GRID_SIZE + 10, self.game.HEIGHT * self.game.GRID_SIZE + 10  # Outside grid
        mouse_event = pygame.event.Event(pygame.MOUSEBUTTONUP, {"pos": (x, y)})
        pygame.event.post(mouse_event)

        board_before = [row[:] for row in self.game.board]  # Copy board state
        self.game.play_game()  # Run the function
        self.assertEqual(self.game.board, board_before)  # Ensure no change in board state

    def test_ai_moves_after_player(self):
        """ Test if the AI makes a move after the player. """
        x, y = self.game.WIDTH // 2, self.game.HEIGHT // 2  # Click in the center of a cell
        col = int(x // (self.game.WIDTH + self.game.MARGIN))
        row = int(y // (self.game.HEIGHT + self.game.MARGIN))

        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONUP, {"pos": (x, y)}))

        self.game.play_game()  # Run the function

        # Ensure both player and AI made a move
        num_moves = sum(cell in ["X", "O"] for row in self.game.board for cell in row)
        self.assertGreaterEqual(num_moves, 2)  # At least two moves made (player + AI)

if __name__ == "__main__":
    unittest.main()
