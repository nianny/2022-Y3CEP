from minimax import Minimax
import options
from player import Player

        
class Game:
    def __init__(self):
        self.game_options = [options.NumGameOptions(2, "Number of players", 2, 5, "How many players do you want to have"), options.NumGameOptions(2, "Number of hands", 2, 5, "How many hands should each player have"), options.ToggleGameOptions(False, "Is spliting allowed")]
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
        
        print()
        print("Game Options:")
        for i in range(len(self.game_options)):
            self.game_options[i].list(i+1)
        
        while True:
            while True:
                try:
                    num = input("Index of game option you want to change (enter to continue): ")
                    if num == '':
                        break
                    num = int(num)
                    if num < 1 or num > len(self.game_options):
                        raise Exception("Invalid input")
            
                    self.game_options[num-1].edit()
                    print()
                    print("Game Options:")
                    for i in range(len(self.game_options)):
                        self.game_options[i].list(i+1)
                    break                    
                except:
                    print("Invalid input.\n")
            
            if num == '':
                break
        
        if mode == 1:
            board = [Player(2, options = self.game_options), Minimax(2, options = self.game_options)] # minimax always as second player (since otherwise person would never win, i think)
            
            # pos represents which player's turn it is
            pos = 0
            while not self.check_win(board):
                split, hand, target, target_hand = board[pos].move(board, pos)
                if not split:
                    board[target].hands[target_hand] += board[pos].hands[hand]
                    if pos == 1:
                        print(f"Player {pos+1} has tapped Player {target+1}'s hand {target_hand+1} with hand {board[pos].hands[hand]}.")
                else:
                    print(hand, board[pos].hands)
                    board[pos].hands = hand
                    
                 # toggle "pos", other possible ways could be to do (pos + 1 )%2
                # do note that this method only works when there are two players (which minimax is limited to)
                pos = int (not pos)
                
            
            for player in range(len(board)):
                if board[player].check_alive():
                    print(f"Player {player+1} wins!")
        
        #previously we already checked that its either 1 or 2 (cannot be anything else)
        else:
            board = []
            # for i in range(players):
            #     board.append(Player(hands))
            
            for i in range(self.game_options[0].value):
                board.append(Player(self.game_options[1].value))
                
            
            pos = 0
            while not self.check_win(board):
                hand, target, target_hand = board[pos].move(board, pos)
                board[target].hands[target_hand] += board[pos].hands[hand]
                
                # toggle "pos", other possible ways could be to do (pos + 1 )%2
                # pos = (pos+1)%players
                pos = (pos+1)%self.game_options[0].value
            
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