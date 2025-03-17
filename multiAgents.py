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

    # Minimizing Player (Other AI Agents)
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
    if (depth == 0) or (terminal):
        scores = game_status.get_negamax_scores(terminal)
        return scores, None

    # Worst possible score at the start of search
    # -inf defines smallest possible value 
    # best_value gets updated with the highest score found 
    best_value = float('-inf')
    best_move = None

    # Loop through the possible moves and apply a set move and return the new board state
    for move in game_status.get_legal_moves():
        new_state = game_status.get_new_state(move)

        # Flip turn_multiplier (-1) to switch user player perspective
        # Flip score for better evaluation for the current player/user
        value, _ = negamax(new_state, depth - 1, -turn_multiplier, -beta, -alpha)
        value = -value

        # If the new move has a higher value than the current best, apply change
        if value > best_value:
            best_value = value
            best_move = move 

        # Alpha keeps track of the highest score and or best move for the maximizing player/user
        # If Alpha >= beta, search will stop. Beta holds the best move for the Min player
        alpha = max(alpha, value)
        if alpha >= beta:
            break  

    # Return the best score and the best move 
    return best_value, best_move
