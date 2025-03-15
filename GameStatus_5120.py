# -*- coding: utf-8 -*-


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		count = 0
		for row in range(rows):
			for col in range(cols):
				if self.board_state[row][col] == 0:
					count += 1
		if count >= 1:
			return False
		# if we have no empty spaces we check who won now with updated score
		self.oldScores = self.get_scores(terminal=True)
		if count == 0:
			if self.oldScores > 0:
				self.winner = "Human wins"
			elif self.oldScores == 0:
				self.winner = "draw"
			else:
				self.winner = "AI wins"
		return self.winner

	def get_scores(self, terminal):
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		Hscore = 0
		AIscore = 0
		check_point = 3 if terminal else 2


		# handles bounds so it doesn't throw outbounds errors
		def in_bounds(rows, cols):
			if rows < 0 or rows >= len(self.board_state) or cols < 0 or cols >= len(self.board_state[0]):
				return False
			else:
				return True
		
		# checking the board for wins
		for row in range(rows):
			for col in range(cols):
				if in_bounds(rows,cols+2):
					# checks rows
					if self.board_state[row][col] == 'x' and self.board_state[row][col+1] == 'x' and self.board_state[row][col+2] == 'x':
						Hscore += 1
					elif self.board_state[row][col] == 'o' and self.board_state[row][col+1] == 'o' and self.board_state[row][col+2] == 'o':
						AIscore += 1
				if in_bounds(rows+2,cols):
					# check columns
					if self.board_state[row][col] == 'x' and self.board_state[row+1][col] == 'x' and self.board_state[row+2][col] == 'x':
						Hscore += 1
					elif self.board_state[row][col] == 'o' and self.board_state[row+1][col] == 'o' and self.board_state[row+2][col] == 'o':
						AIscore += 1
				# check diagonals
				# left diag
				if in_bounds(rows+2,cols+2):
					if self.board_state[row][col] == 'x' and self.board_state[row+1][col+1] == 'x' and self.board_state[row+2][col+2] == 'x':
						Hscore += 1
					elif self.board_state[row][col] == 'o' and self.board_state[row+1][col+1] == 'o' and self.board_state[row+2][col+2] == 'o':
						AIscore += 1
				# right diag
				if in_bounds(rows+2,cols-2):
					if self.board_state[row][col] == 'x' and self.board_state[row+1][col-1] == 'x' and self.board_state[row+2][col-2] == 'x':
						Hscore += 1
					elif self.board_state[row][col] == 'o' and self.board_state[row+1][col-1] == 'o' and self.board_state[row+2][col-2] == 'o':
						AIscore += 1
		# gets score and put it in the global variable of scores so it can be used by other functions
		scores = Hscore - AIscore
		self.oldScores = scores
		return self.oldScores
		
	    

	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
	    

	def get_moves(self):
		moves = []

		# go over the board to find non-empty cells
		for row in range(3):
			for col in range(3):
				# check if the cell is empty
				if self.board[row][col] == ' ':
					# if empty, add to list of possible moves
					moves.append((row, col))

		return moves


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x,y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
