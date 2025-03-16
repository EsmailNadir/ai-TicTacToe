"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

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
        self.game_reset()

    def draw_game(self):
        """ Draws the game grid and initializes the display. """
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        """
        YOUR CODE HERE TO DRAW THE GRID AND OTHER CONTROLS AS PART OF THE GUI.
        """

        pygame.display.update()

    def change_turn(self):
        """ Changes the turn and updates the display title accordingly. """
        if self.game_state.turn_O:
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")

    def draw_circle(self, x, y):
        """ 
        YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER.
        """
        pass  # Implement the drawing logic here.

    def draw_cross(self, x, y):
        """ 
        YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL SELECTED VIA THE GUI.
        """
        pass  # Implement the drawing logic here.

    def is_game_over(self):
        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE.
        YOU SHOULD USE THE is_terminal() FUNCTION FROM GameStatus_5120.PY FILE.
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME.
        """
        return self.game_state.is_terminal()

    def move(self, move):
        """ Updates the game state with the new move. """
        self.game_state = self.game_state.get_new_state(move)

    def play_ai(self):

        if mode == "minimax":
            _, best_move = minimax(self.game_state, depth=3, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf'))
        elif mode == "negamax":
            _, best_move = negamax(self.game_state, depth=3, turn_multiplier=1, alpha=float('-inf'), beta=float('inf'))
        else:
            return  # No valid mode selected

        if best_move:
            self.move(best_move)
            x, y = best_move

            self.draw_circle(x, y)  # Assuming AI uses circles

            self.change_turn()
            pygame.display.update()

        if self.is_game_over():
            terminal = self.game_state.is_terminal()
            final_score = self.game_state.get_scores(terminal)
            print(f"Game Over! Final Score: {final_score}")

        pygame.display.update()

    def game_reset(self):
        """
        Resets the board to value 0 for all cells and creates a new game state.
        """
        self.draw_game()

        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE.
        """

        pygame.display.update()

    def play_game(self, mode="player_vs_ai"):
        """ Main game loop that listens for user events and updates the game state accordingly. """
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():  # User interaction handling
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM.
                EXIT THE GAME IF THE USER CLICKED EXIT.
                """

                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER.
                DISPLAY THE SCORE, WINNER, AND WAIT FOR THE USER TO RESET THE BOARD OR EXIT.
                """

                """
                YOUR CODE HERE TO CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON-EMPTY CELL.
                IF CLICKED ON A NON-EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON SYMBOL SELECTED FROM THE GUI), AND CALL play_ai() FUNCTION.
                """

                # Example structure:
                # if event.type == pygame.MOUSEBUTTONUP:
                #     # Get the position of the click
                #     x, y = pygame.mouse.get_pos()
                #     # Convert screen coordinates to grid coordinates
                #     grid_x = x // (self.WIDTH + self.MARGIN)
                #     grid_y = y // (self.HEIGHT + self.MARGIN)
                #     # Process the move if it's valid
                #     if self.game_state.board_state[grid_x][grid_y] == 0:
                #         self.move((grid_x, grid_y))
                #         self.draw_cross(grid_x, grid_y)
                #         self.play_ai()

            pygame.display.update()

        pygame.quit()


# Initialize and start the game
tictactoegame = RandomBoardTicTacToe()

"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE.
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME.
YOUR FUNCTION play_game() SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME.
"""
