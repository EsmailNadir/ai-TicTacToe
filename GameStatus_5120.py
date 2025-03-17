# -*- coding: utf-8 -*-
class GameStatus:
    def __init__(self, board_state, turn_O):
        self.board_state = board_state
        self.turn_O = turn_O
        self.oldScores = 0
        self.winner = ""
    
    def is_terminal(self):
       
        # Check for a winner
        rows = len(self.board_state)
        cols = len(self.board_state[0])
        
        # Check horizontal, vertical, and diagonal lines for a win
        # Horizontal
        for row in range(rows):
            for col in range(cols - 3):
                if self.board_state[row][col] != 0 and self.board_state[row][col] == self.board_state[row][col+1] == self.board_state[row][col+2] == self.board_state[row][col+3]:
                    self.winner = "O" if self.board_state[row][col] == 1 else "X"
                    return True
        
        # Vertical
        for row in range(rows - 3):
            for col in range(cols):
                if self.board_state[row][col] != 0 and self.board_state[row][col] == self.board_state[row+1][col] == self.board_state[row+2][col] == self.board_state[row+3][col]:
                    self.winner = "O" if self.board_state[row][col] == 1 else "X"
                    return True
        
        # Diagonal (top-left to bottom-right)
        for row in range(rows - 3):
            for col in range(cols - 3):
                if self.board_state[row][col] != 0 and self.board_state[row][col] == self.board_state[row+1][col+1] == self.board_state[row+2][col+2] == self.board_state[row+3][col+3]:
                    self.winner = "O" if self.board_state[row][col] == 1 else "X"
                    return True
        
        # Diagonal (top-right to bottom-left)
        for row in range(rows - 3):
            for col in range(3, cols):
                if self.board_state[row][col] != 0 and self.board_state[row][col] == self.board_state[row+1][col-1] == self.board_state[row+2][col-2] == self.board_state[row+3][col-3]:
                    self.winner = "O" if self.board_state[row][col] == 1 else "X"
                    return True
        
        # Check if there are any empty cells left
        for row in range(rows):
            for col in range(cols):
                if self.board_state[row][col] == 0:
                    return False  # Game is not over yet
        
        # If we get here, the board is full but no winner
        self.winner = "Draw"
        return True

    def get_scores(self, terminal):
        rows = len(self.board_state)
        cols = len(self.board_state[0])
        scores = 0
        check_point = 3 if terminal else 2
        
        # Check for wins and potential wins in all directions
        
        # Horizontal
        for row in range(rows):
            for col in range(cols - 3):
                window = [self.board_state[row][col+i] for i in range(4)]
                scores += self._evaluate_window(window)
        
        # Vertical
        for row in range(rows - 3):
            for col in range(cols):
                window = [self.board_state[row+i][col] for i in range(4)]
                scores += self._evaluate_window(window)
        
        # Diagonal (top-left to bottom-right)
        for row in range(rows - 3):
            for col in range(cols - 3):
                window = [self.board_state[row+i][col+i] for i in range(4)]
                scores += self._evaluate_window(window)
        
        # Diagonal (top-right to bottom-left)
        for row in range(rows - 3):
            for col in range(3, cols):
                window = [self.board_state[row+i][col-i] for i in range(4)]
                scores += self._evaluate_window(window)
        
        return scores * check_point
    
    def _evaluate_window(self, window):
        """Helper method to evaluate a window of 4 positions"""
        score = 0
        
        # Count pieces in the window
        x_count = window.count(-1)
        o_count = window.count(1)
        empty_count = window.count(0)
        
        # Score the window
        if o_count == 4:
            score -= 100  # AI wins
        elif o_count == 3 and empty_count == 1:
            score -= 10   # AI potential win
        elif o_count == 2 and empty_count == 2:
            score -= 1    # AI building up
            
        if x_count == 4:
            score += 100  # Human wins
        elif x_count == 3 and empty_count == 1:
            score += 10   # Human potential win
        elif x_count == 2 and empty_count == 2:
            score += 1    # Human building up
            
        return score

    def get_negamax_scores(self, terminal):
        return self.get_scores(terminal)  # Use the same scoring function for simplicity

    def get_legal_moves(self):
        moves = []
        
        # Find all empty cells (with value 0)
        for row in range(len(self.board_state)):
            for col in range(len(self.board_state[row])):
                if self.board_state[row][col] == 0:
                    moves.append((row, col))
        
        return moves

    def get_new_state(self, move):
       
        # Create a deep copy of the board
        new_board_state = [row[:] for row in self.board_state]
        
        # Apply the move
        row, col = move
        new_board_state[row][col] = 1 if self.turn_O else -1
        
        # Return a new state with the move applied and turn switched
        return GameStatus(new_board_state, not self.turn_O)