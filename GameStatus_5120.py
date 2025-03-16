# -*- coding: utf-8 -*-


class GameStatus:
    def __init__(self, board_state, turn_O):
        self.board_state = board_state
        self.turn_O = turn_O
        self.oldScores = 0
        self.winner = ""

    def is_terminal(self):
        """
        YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. 
        IF THERE IS NO EMPTY CELL, THEN YOU SHOULD ALSO RETURN THE WINNER 
        OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER.
        """
        pass  

    def get_scores(self, terminal):
        """
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE 
        FOR EACH PLAYER BY CHECKING EACH TRIPLET IN THE BOARD IN EACH 
        DIRECTION (HORIZONTAL, VERTICAL, AND ANY DIAGONAL DIRECTION).

        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE:
        - POSITIVE (HUMAN PLAYER WINS)
        - NEGATIVE (AI PLAYER WINS)
        - 0 (DRAW)
        """        
        rows = len(self.board_state)
        cols = len(self.board_state[0])
        scores = 0
        check_point = 3 if terminal else 2
        return scores  

    def get_negamax_scores(self, terminal):
        """
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY 
        BE THE SAME AS GET_SCORES UNLESS YOU SET THE SCORE FOR NEGAMAX TO A VALUE 
        THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES += 100 
        FOR HUMAN PLAYER INSTEAD OF SCORES += 1)
        """  
        rows = len(self.board_state)
        cols = len(self.board_state[0])
        scores = 0
        check_point = 3 if terminal else 2

        # Loops through each row and column across the board  
        for row in range(rows):
            for col in range(cols):		
                if self.board_state[row][col] == "X":
                    # "X" represents a move by the human player/user
                    # Prioritize human player's move in evaluation to adjust AI strategy
                    scores += 100
                # If "O" is ever contained, that means it is being occupied by the AI 
                # Decreasing the score benefits access for the AI
                elif self.board_state[row][col] == "O":
                    scores -= 100

        return scores * check_point  

    def get_moves(self):
        """
        YOUR CODE HERE TO ADD ALL THE NON-EMPTY CELLS TO MOVES VARIABLES 
        AND RETURN IT TO BE USED BY YOUR MINIMAX OR NEGAMAX FUNCTIONS.
        """
        moves = []
        return moves  

    def get_new_state(self, move):
        new_board_state = [row[:] for row in self.board_state]  
        x, y = move[0], move[1]
        new_board_state[x][y] = 1 if self.turn_O else -1  
        return GameStatus(new_board_state, not self.turn_O)
