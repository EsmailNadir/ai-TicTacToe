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
        self.size = self.width, self.height = size

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 4
        self.OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0] / self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1] / self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()

    
        self.board = [[""] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]

        self.game_reset()

    def draw_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        # Create the grid lines for the Tic Tac Toe board
        cell_size = self.size[0] // len(self.board)
        line_thickness = max(2, cell_size // 30)

        for i in range(1, len(self.board)):
            pygame.draw.line(
                self.screen, self.WHITE, (i * cell_size, 0),
                (i * cell_size, self.size[1]), line_thickness
            )
            pygame.draw.line(
                self.screen, self.WHITE, (0, i * cell_size),
                (self.size[0], i * cell_size), line_thickness
            )

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
        if self.game_state.turn_O:
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")

    def draw_circle(self, x, y):
        pass  

    def draw_cross(self, x, y):
        pass  

    def is_game_over(self):
        return self.game_state.is_terminal()

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)

    def play_ai(self):
        if mode == "minimax":
            _, best_move = minimax(self.game_state, depth=3, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf'))
        elif mode == "negamax":
            _, best_move = negamax(self.game_state, depth=3, turn_multiplier=1, alpha=float('-inf'), beta=float('inf'))
        else:
            return  

        if best_move:
            self.move(best_move)
            x, y = best_move

            self.draw_circle(x, y)  

            self.change_turn()
            pygame.display.update()

        if self.is_game_over():
            terminal = self.game_state.is_terminal()
            final_score = self.game_state.get_scores(terminal)
            print(f"Game Over!! Final Score: {final_score}")

        pygame.display.update()

    def game_reset(self):
        self.draw_game()
        pygame.display.update()

    def play_game(self, mode="player_vs_ai"):
        
        self.board = [[""] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]  
        
        done = False  
        clock = pygame.time.Clock()  

        while not done:
            for event in pygame.event.get():
                # If the window gets closed by the player, game loop will exit
                if event.type == pygame.QUIT:
                    done = True

                # Screen X and Y are coordinated to the board column and row
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    
                    col = int(x // (self.WIDTH + self.MARGIN))  
                    row = int(y // (self.HEIGHT + self.MARGIN))  

                    # Check if the click is inside the board boundaries
                    if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
                        if self.board[row][col] == "":  
                            # Assign the human player's move
                            self.board[row][col] = "X"  
                            # Draw an X for the clicked position 
                            self.draw_cross(col, row)  

                            # Check if the game is over after the player finishes the move 
                            if self.is_game_over():
                                terminal = self.game_state.is_terminal()
                                final_score = self.game_state.get_scores(terminal)
                                print(f"Game Over!! Final Score: {final_score}")
                                pygame.display.update()
                                pygame.time.delay(3000) 
                                return  

                            # Switch to the AI's turn 
                            self.change_turn()  
                            # Call the AI move function
                            self.play_ai()  

            # This is the refresh display       
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
