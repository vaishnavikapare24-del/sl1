def alphabeta_pruning(depth, node_index, maximizing_player, values, alpha, beta):

    if depth == 0 or node_index >= len(values):
        return values[node_index]
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = alphabeta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alphabeta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

values = [2,3,5,9,0,1,7,5]
depth = 3
optimal_evaluation = alphabeta_pruning(depth, 0, True, values, float('-inf'), float('inf'))
print(f"The optimal evaluation is {optimal_evaluation}")
