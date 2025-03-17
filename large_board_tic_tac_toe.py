import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai"  # Default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size=(600, 600)):
        self.size = self.width, self.height = size

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid size and offset
        self.GRID_SIZE = 4
        self.OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # Cell size calculation
        self.WIDTH = self.size[0] / self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1] / self.GRID_SIZE - self.OFFSET

        # Margin between grid cells
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()

        # Initialize game components
        self.board = [[""] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        self.game_state = GameStatus(board_state=[[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)], turn_O=False)
        self.current_player = "X"  # Track the current player

        # Create the screen
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe")

        # Now it's safe to reset the game
        self.game_reset()

    def game_reset(self):
        self.board = [[""] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        self.game_state = GameStatus(board_state=[[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)], turn_O=False)
        self.current_player = "X"
        self.draw_game()
        pygame.display.update()

    def draw_game(self):
        self.screen.fill(self.BLACK)

        # Determine cell size
        cell_size = self.size[0] // self.GRID_SIZE
        line_thickness = max(2, cell_size // 30)

        # Draw grid lines
        for i in range(1, self.GRID_SIZE):
            pygame.draw.line(self.screen, self.WHITE, (i * cell_size, 0),
                             (i * cell_size, self.size[1]), line_thickness)
            pygame.draw.line(self.screen, self.WHITE, (0, i * cell_size),
                             (self.size[0], i * cell_size), line_thickness)

        # Render X and O moves
        font = pygame.font.Font(None, int(cell_size * 0.7))
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                move = self.board[row][col]
                if move == "X" or move == "O":
                    text = font.render(move, True, self.WHITE)
                    text_rect = text.get_rect(center=((col * cell_size) + cell_size // 2,
                                                      (row * cell_size) + cell_size // 2))
                    self.screen.blit(text, text_rect)

        pygame.display.update()

    def change_turn(self):

        self.current_player = "O" if self.current_player == "X" else "X"
        self.game_state.turn_O = not self.game_state.turn_O

    def make_move(self, row, col):
        if 0 <= row < self.GRID_SIZE and 0 <= col < self.GRID_SIZE:
            if self.board[row][col] == "":
                # Update the visual board
                self.board[row][col] = self.current_player
                
                # Update the game state board
                self.game_state.board_state[row][col] = 1 if self.current_player == "O" else -1
                
                # Draw the move
                self.draw_game()
                
                # Check for game over
                if self.is_game_over():
                    winner = self.game_state.winner
                    if winner == "Draw":
                        print("Game Over! It's a draw!")
                    else:
                        print(f"Game Over! {winner} wins!")
                    pygame.time.delay(3000)
                    return True
                
                # Change turn
                self.change_turn()
                return True
        return False

    def play_ai(self):
        if self.is_game_over():
            return False
            
        try:
            if mode == "minimax":
                _, best_move = minimax(self.game_state, depth=3, maximizingPlayer=False, alpha=float('-inf'), beta=float('inf'))
            else:  # Default to negamax
                _, best_move = negamax(self.game_state, depth=3, turn_multiplier=-1, alpha=float('-inf'), beta=float('inf'))
                
            if best_move:
                row, col = best_move
                # Make the move directly
                self.board[row][col] = "O"  # AI move
                self.game_state.board_state[row][col] = 1  # Update game state (1 for O)
                
                # Update display
                self.draw_game()
                print(f"AI played at: {row}, {col}")
                
                # Check for game over
                if self.is_game_over():
                    winner = self.game_state.winner
                    if winner == "Draw":
                        print("Game Over! It's a draw!")
                    else:
                        print(f"Game Over! {winner} wins!")
                    pygame.time.delay(3000)
                    return True
                    
                # Change turn
                self.change_turn()
                return True
            else:
                print("AI couldn't find a move!")
                return False
        except Exception as e:
            print(f"Error in AI move: {e}")
            return False

    def is_game_over(self):
        return self.game_state.is_terminal()

    def play_game(self, mode="player_vs_ai"):
        print("Game is starting...")
        self.screen.fill(self.BLACK)
        self.draw_game()
        pygame.display.update()

        done = False
        clock = pygame.time.Clock()
        game_over = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting game...")
                    done = True

                elif event.type == pygame.MOUSEBUTTONUP and not game_over:
                    # Only handle mouse events if it's the player's turn
                    if mode == "player_vs_player" or (mode == "player_vs_ai" and self.current_player == "X"):
                        x, y = pygame.mouse.get_pos()
                        print(f"Mouse clicked at: {x}, {y}")

                        col = int(x // (self.width / self.GRID_SIZE))
                        row = int(y // (self.height / self.GRID_SIZE))

                        if self.make_move(row, col):
                            if self.is_game_over():
                                game_over = True
                            elif mode == "player_vs_ai" and self.current_player == "O":
                                print("AI is thinking...")
                                pygame.time.delay(1000)  # Delay before AI moves
                                if self.play_ai():
                                    if self.is_game_over():
                                        game_over = True

            # If it's AI's turn in player_vs_ai mode
            if mode == "player_vs_ai" and self.current_player == "O" and not game_over and not done:
                print("AI is thinking...")
                pygame.time.delay(1000)  # Delay before AI moves
                if self.play_ai():
                    if self.is_game_over():
                        game_over = True

            pygame.display.update()
            clock.tick(30)

            # If game is over, wait and then reset
            if game_over:
                pygame.time.delay(3000)
                self.game_reset()
                game_over = False

        pygame.quit()


# Initialize and start the game
tictactoegame = RandomBoardTicTacToe()

def select_game_mode():
    global mode
    print("Select game mode:")
    print("1. Player vs AI")
    print("2. Player vs Player")
    choice = input("Enter choice (1/2): ")
    if choice == "1":
        mode = "player_vs_ai"
    elif choice == "2":
        mode = "player_vs_player"

if __name__ == "__main__":
    select_game_mode()
    tictactoegame.play_game(mode)