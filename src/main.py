from minimax import Minimax
import options
from player import Player

        
class Game:
    game_options = [options.ToggleGameOptions(True, "Is spliting allowed? ")]
    
    def __init__(self):
        print("""
Hallooooo and welcome to this very scuffed game of chopsticks :O 
There are various modes you can play, including playing against a cool bot to learn how to win every game!!!

What mode would you like to play?   
1) Play against a bot
2) Play against other players
""")
        while True:
            try:
                mode = int(input("Input either 1 or 2: "))
                if not (mode == 1 or mode == 2):
                    raise Exception("Invalid input")
                break
            except:
                print("Invalid input.\n")
        
        players = 2
        hands = 2
        if mode == 1:
            board = [Player(2), Minimax(2)] # minimax always as second player (since otherwise person would never win, i think)
            
            # pos represents which player's turn it is
            pos = 0
            while not self.check_win(board):
                split, hand, target, target_hand = board[pos].move(board, pos)
                if not split:
                    board[target].hands[target_hand] += board[pos].hands[hand]
                    
                    if pos == 1:
                        print(f"Player {pos+1} has tapped Player {target+1}'s hand {target_hand+1} with hand {board[pos].hands[hand]}.")
                    
                    # toggle "pos", other possible ways could be to do (pos + 1 )%2
                    # do note that this method only works when there are two players (which minimax is limited to)
                    pos = int (not pos)
            
            for player in range(len(board)):
                if board[player].check_alive():
                    print(f"Player {player+1} wins!")
        
        #previously we already checked that its either 1 or 2 (cannot be anything else)
        else:
            board = []
            for i in range(players):
                board.append(Player(hands))
            
            pos = 0
            while not self.check_win(board):
                hand, target, target_hand = board[pos].move(board, pos)
                board[target].hands[target_hand] += board[pos].hands[hand]
                
                # toggle "pos", other possible ways could be to do (pos + 1 )%2
                pos = (pos+1)%players
            
            for player in range(len(board)):
                if board[player].check_alive():
                    print(f"Player {player+1} wins!")


    
    def check_win(self, board):
        alive_counter = 0
        for player in board:
            if player.check_alive():
                alive_counter += 1
                    
        if alive_counter > 1:
            return False
        else:
            return True
game = Game()