"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING.

The file where you will need to create the GUI which should include:
(i) Drawing the grid
(ii) Calling your Minimax/Negamax functions at each step of the game
(iii) Allowing the controls on the GUI to be managed (e.g., setting board size, using Minimax or Negamax, and other options)

In the example below, grid creation is supported using pygame, which you can use.
You are free to use any other library to create a better-looking GUI with more control.

In the __init__ function, GRID_SIZE (Line number 36) is the variable that sets the size of the grid.
Once you have the Minimax code written in multiAgents.py file, it is recommended to test
your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw
and does not let you win the game.

Here is a video tutorial for using pygame to create grids: http://youtu.be/mdTeqiWyFnc

PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS.
"""

import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai"  # Default mode for playing the game (player vs AI)


class RandomBoardTicTacToe:
    def __init__(self, size=(600, 600)):
        """ Initialize the game window and board properties. """
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

        self.board = [[""] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        self.game_reset()

    def draw_game(self):
        """ Draws the Tic Tac Toe grid and updates the display with player moves. """
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        # Determine cell size
        cell_size = self.size[0] // len(self.board)
        line_thickness = max(2, cell_size // 30)

        # Draw grid lines
        for i in range(1, len(self.board)):
            pygame.draw.line(self.screen, self.WHITE, (i * cell_size, 0),
                             (i * cell_size, self.size[1]), line_thickness)
            pygame.draw.line(self.screen, self.WHITE, (0, i * cell_size),
                             (self.size[0], i * cell_size), line_thickness)

        # Render X and O moves
        font = pygame.font.Font(None, int(cell_size * 0.7))
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                move = self.board[row][col]
                if move == "X" or move == "O":
                    text = font.render(move, True, self.WHITE)
                    text_rect = text.get_rect(center=((col * cell_size) + cell_size // 2,
                                                      (row * cell_size) + cell_size // 2))
                    self.screen.blit(text, text_rect)

        pygame.display.update()

    def change_turn(self):
        """ Updates the game window title to indicate the current player's turn. """
        if self.game_state.turn_O:
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")

    def draw_circle(self, x, y):
        """ Draws a circle (O) at the given grid position. """
        pass

    def draw_cross(self, x, y):
        """ Draws a cross (X) at the given grid position. """
        pass

    def is_game_over(self):
        """ Checks if the game has reached a terminal state. """
        return self.game_state.is_terminal()

    def move(self, move):
        """ Updates the game state with the player's move. """
        self.game_state = self.game_state.get_new_state(move)

    def play_ai(self):
        """ Calls the AI to make a move using either Minimax or Negamax. """
        if mode == "minimax":
            _, best_move = minimax(self.game_state, depth=3, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf'))
        elif mode == "negamax":
            _, best_move = negamax(self.game_state, depth=3, turn_multiplier=1, alpha=float('-inf'), beta=float('inf'))
        else:
            return  

        if best_move:
            self.move(best_move)
            x, y = best_move
            self.draw_circle(x, y)  # Assuming AI plays as 'O'
            self.change_turn()
            pygame.display.update()

        if self.is_game_over():
            terminal = self.game_state.is_terminal()
            final_score = self.game_state.get_scores(terminal)
            print(f"Game Over!! Final Score: {final_score}")

        pygame.display.update()

    def game_reset(self):
        """ Resets the game board and updates the display. """
        self.draw_game()
        if self.is_game_over():
            board_size = self.GRID_SIZE
            self.game_state = GameStatus(board_state=[[0] * board_size for _ in range(board_size)], turn_O=False)
            self.game_over = False
        pygame.display.update()

    def play_game(self, mode="player_vs_ai"):
        """ Main game loop that handles user inputs and updates the game state accordingly. """
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                # Identify quit event 
                if event.type == pygame.QUIT:
                    done = True

                # Check for the mouse clicks 
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    col = int(x // (self.WIDTH + self.MARGIN))
                    row = int(y // (self.HEIGHT + self.MARGIN))

                    # Ensure click is inside board boundaries
                    if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
                        if self.board[row][col] == "":
                            self.board[row][col] = "X"
                            self.draw_cross(col, row)

                            # Check if the game is over after moves
                            if self.is_game_over():
                                terminal = self.game_state.is_terminal()
                                final_score = self.game_state.get_scores(terminal)
                                print(f"Game Over! Final Score: {final_score}")
                                pygame.display.update()
                                pygame.time.delay(3000)
                                return  

                            # Switch to AI's turn etc
                            self.change_turn()
                            self.play_ai()

            pygame.display.update()
            clock.tick(30)

        pygame.quit()


# Initialize and start the game
tictactoegame = RandomBoardTicTacToe()

"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE.
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME.
YOUR FUNCTION play_game() SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME.
"""
