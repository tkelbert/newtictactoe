import math


class TakeAwayGame:
    def __init__(self, initial_items):
        """Initializes the game state.

        Args:
            initial_items (int): The starting number of items in the pile.
        """
        self.items = initial_items
        self.current_player = 1
        # TODO: Initialize self.items
        # TODO: Initialize self.current_player (start with player 1)
        print(f"Game started with {initial_items} items. Player {self.current_player}'s turn.") # Optional: for feedback

    def make_move(self, number_to_take):
        """Attempts to remove items from the pile.

        Args:
            number_to_take (int): The number of items the current player tries to take (1, 2, or 3).

        Returns:
            bool: True if the move was valid and executed, False otherwise.
        """
        # Validate the number_to_take (must be 1, 2, or 3)
        if number_to_take < 1 or number_to_take > 3:
            return False
        
        
        #  Validate the number_to_take (must be <= self.items)
        if number_to_take <= self.items:
        #  If valid:
            self.items -= number_to_take
            
            print(f"player {self.current_player} took {number_to_take} items. {self.items} remain")
        #    Update self.items
        #    Switch self.current_player (e.g., 1 becomes 2, 2 becomes 1)
            if self.current_player == 1:
                self.current_player = 2
            else:
                self.current_player = 1
            
        #  Print status (Optional: "Player X took Y items. Z items remain.")
        #   Return True
            return True
        else:#
            return False

    def is_game_over(self):
        if self.items <= 0:
            return True
        else: 
            return False
        
    def get_winner(self):
        if self.current_player == 1:
            last_player = 2
        else:
            last_player = 1
        if self.items > 0:
            return None
        return last_player

# --- Minimax with Visualization ---
def minimax(items, is_maximizing, depth=0): # Add depth parameter
    indent = "  " * depth # Create indentation string

    # --- Base Case: Game Over ---
    if items == 0:
        score = -1 if is_maximizing else 1
        print(f"{indent}Base Case: items=0. Returning score: {score}")
        return score

    # --- Recursive Step ---
    if is_maximizing: # AI's turn (Maximizer)
        print(f"{indent}Maximizer evaluating state: items={items}")
        max_eval = float('-inf')
        for move in range(1, 4):
            if move <= items:
                items_after_move = items - move
                print(f"{indent}  Considering move {move} (items become {items_after_move})")
                # Recursive call (increase depth)
                score = minimax(items_after_move, False, depth + 1)
                print(f"{indent}  Got score {score} for move {move}")
                max_eval = max(max_eval, score)
            # else: # Optional: print if move is invalid
            #    print(f"{indent}  Move {move} is invalid (items={items})")
        print(f"{indent}Maximizer result for items={items}: {max_eval}")
        return max_eval

    else: # Opponent's turn (Minimizer)
        print(f"{indent}Minimizer evaluating state: items={items}")
        min_eval = float('inf')
        for move in range(1, 4):
            if move <= items:
                items_after_move = items - move
                print(f"{indent}  Considering move {move} (items become {items_after_move})")
                # Recursive call (increase depth)
                score = minimax(items_after_move, True, depth + 1)
                print(f"{indent}  Got score {score} for move {move}")
                min_eval = min(min_eval, score)
            # else: # Optional: print if move is invalid
            #    print(f"{indent}  Move {move} is invalid (items={items})")
        print(f"{indent}Minimizer result for items={items}: {min_eval}")
        return min_eval

# --- Find Best Move with Visualization ---
def find_best_move(game):
    """
    Finds the best move for the AI player (Maximizer) in the current game state.
    """
    print(f"\n--- AI finding best move for {game.items} items ---")
    best_score = float('-inf')
    best_move = -1

    # Loop through possible moves AI can make (1, 2, 3)
    for move in range(1, 4):
        if move <= game.items:
            items_after_move = game.items - move
            print(f"Evaluating move: {move} (items after move: {items_after_move})")
            # Evaluate this resulting state using minimax. Start recursion at depth 0.
            # Since AI (Maximizer) is making the move, the next turn belongs to the Minimizer.
            score = minimax(items_after_move, False, depth=0) # Start minimax call
            print(f"  Move {move} evaluated to score: {score}")

            if score > best_score:
                print(f"  >>> Found new best move: {move} with score {score} (previous best score: {best_score})")
                best_score = score
                best_move = move

    print(f"--- AI decision: best move is {best_move} (score: {best_score}) ---")
    return best_move
                   
        
game = TakeAwayGame(10)

while not game.is_game_over():
    print("==============================================")
    print("==============================================")
    print(f"the current number of items is: {game.items} ")
    print(f"it is the player {game.current_player}'s turn")
    if game.current_player == 1:
        taken = input("how many items would you like to take? > ")
        try:
            taken = int(taken)
        except:
            print(f"you must enter a valid integer")
            continue

        if not game.make_move(taken):
            if taken < 1 or taken > 3:
                print(f"error: wrong amount, must be an integer between 1 and 3")
            if game.items <=3:
                print(f"remember that your move must be less than the total number of items ({game.items})")
    else:
        ai_move = find_best_move(game)
        print(f"the very smart AI divines the move: {ai_move}")
        game.make_move(ai_move)


print("===========================")
print("calculating winner...")

winner = game.get_winner()

if winner is not None:
    print(f"game over, player {winner} wins!")
else:
    print("game over, could not determine winner")

