from minimax import Minimax
            
             
            
        
def check_win(board):
    alive_counter = 0
    for player in board:
        if player.check_alive():
            alive_counter += 1
                
    if alive_counter > 1:
        return True
    else:
        return False
    
class Player:
    def __init__(self, hand_number = 2, hand = None):
        if hand != None:
            self.hands = hand
        else:
            self.hands = [1]*hand_number
    
    def __eq__(self, __o: object):
        return self.hands == __o.hands
    
    def __repr__(self):
        return str(self.hands)
    
    def copy(self):
        return Player(hand=self.hands.copy())
    
    def check_hand(self):
        for hand in range(len(self.hands)):
            if self.hands[hand] >= 5:
                self.hands[hand] = 0
    
    def check_alive(self):
        self.check_hand()
        for hand in self.hands:
            if hand > 0:
                return True
        return False
    
    def get_hand_num(self):
        return len(self.hands)
    
    def get_hands(self):
        return self.hands
class GameOptions:
    def __init__(self):
        self.
class Game:
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
            mini = Minimax()
game = Game()