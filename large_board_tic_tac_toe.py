"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 4
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
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
            # The vertical lines for the board will be created here
            pygame.draw.line(
                self.screen, self.WHITE, (i * cell_size, 0), 
                (i * cell_size, self.size[1]), line_thickness
            )
            # The horizontal lines for the board will be created here
            pygame.draw.line(
                self.screen, self.WHITE, (0, i * cell_size), 
                (self.size[0], i * cell_size), line_thickness
            )

        # Display and draw out the board moves using "X" and "O"
        font = pygame.font.Font(None, int(cell_size * 0.7))  

        # Loop created to identify player moves throughout the self.board
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                move = self.board[row][col]
                if move == "X" or move == "O":
                    text = font.render(move, True, self.WHITE)  
                    # Centers the positioning horizontally and vertically
                    text_rect = text.get_rect(center=((col * cell_size) + cell_size // 2,
                                                      (row * cell_size) + cell_size // 2))
                    self.screen.blit(text, text_rect)  

        pygame.display.update()  

    def change_turn(self):
        """ Changes the turn and updates the display title accordingly. """
        if self.game_state.turn_O:
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        # this creates a circle with outline
        radius = 50
        pygame.draw.circle(self.screen,self.CIRCLE_COLOR,(x,y),radius,5)
        pygame.draw.circle(self.screen,"blue",(x,y),radius-10,5)
        

    def draw_cross(self, x, y):
        # left side
        pygame.draw.rect(self.screen, "red", (x-20, y+20,15,10))
        pygame.draw.rect(self.screen, self.CROSS_COLOR, (x-10, y+10,15,10))
        pygame.draw.rect(self.screen, "red", (x-20, y-20,15,10))
        pygame.draw.rect(self.screen, self.CROSS_COLOR, (x-10, y-10,15,10))
        # mid
        pygame.draw.rect(self.screen, self.CROSS_COLOR, (x, y,15,15))
        #right side
        pygame.draw.rect(self.screen, self.CROSS_COLOR, (x+10, y-10,15,10))
        pygame.draw.rect(self.screen, "red", (x+20, y-20,15,10))
        pygame.draw.rect(self.screen, self.CROSS_COLOR, (x+10, y+10,15,10))
        pygame.draw.rect(self.screen, "red", (x+20, y+20,15,10))
        
        

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
    

    def move(self, move):
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
        self.draw_game()
        self.board = [["" for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        self.game_state = GameStatus(self.board)  # start a new game state

        self.draw_game()
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()


        while not done:
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                    
                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                
                # if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    
                    # Change the x/y screen coordinates to grid coordinates
                    
                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()

def select_game_mode():
    global mode
    # Ask the user to select the mode
    print("Select game mode:")
    print("1. Player vs AI")
    print("2. Player vs Player")
    choice = input("Enter choice (1/2): ")
    if choice == "1":
        mode = "player_vs_ai"
    elif choice == "2":
        mode = "player_vs_player"

# Start the game by selecting the mode
select_game_mode()
tictactoegame.play_game(mode)
