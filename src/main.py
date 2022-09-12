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
         
        if mode == 1:
            board = [Player(2), Minimax(2)] # minimax always as second player (since otherwise person would never win, i think)
            
            # pos represents which player's turn it is
            pos = 0
            while not self.check_win(board):
                hand, target, target_hand = board[pos].move(board, pos)
                board[target].hands[target_hand] += board[pos].hands[hand]
                
                # toggle "pos", other possible ways could be to do (pos + 1 )%2
                pos = int (not pos)

    
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