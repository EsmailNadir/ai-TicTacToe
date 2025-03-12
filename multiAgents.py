from GameStatus_5120 import GameStatus

from GameStatus_5120 import GameStatus

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
  
   
    terminal = game_state.is_terminal()  # Check if the game is over

    # Base Case: If game over or max depth reached
    if (depth == 0) or terminal:
        newScores = game_state.get_scores(terminal)
        return newScores, None  # No move needed at this point

    # Maximizing Player (Agent 0 - Human or AI-1)
    if maximizingPlayer:
        best_value = float("-inf")
        best_move = None

        for move in game_state.get_moves():  # Loop through all possible moves
            new_state = game_state.get_new_state(move)  # Simulate the move
            eval_value, _ = minimax(new_state, depth - 1, False, alpha, beta)  # Switch to minimizing player

            if eval_value > best_value:
                best_value = eval_value
                best_move = move

            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break  # Prune remaining branches

        return best_value, best_move

    # Minimizing Players (Other AI Agents)
    else:
        worst_value = float("inf")
        worst_move = None

        for move in game_state.get_moves():  # Loop through all possible moves
            new_state = game_state.get_new_state(move)  # Simulate the move
            eval_value, _ = minimax(new_state, depth - 1, True, alpha, beta)  # Switch back to maximizing player

            if eval_value < worst_value:
                worst_value = eval_value
                worst_move = move

            beta = min(beta, eval_value)
            if beta <= alpha:
                break  # Prune remaining branches

        return worst_value, worst_move

        
        
        

	

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
    #return value, best_move