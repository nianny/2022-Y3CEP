class Game: # players, moves
    def __init__(self, player, hand):
        self.player = player
        self.hand = hand
        self.players = []
    
    def run(self):
        print("""
HALLLOOOOOOOOOO :D -----------------------------------------------------------------------------
Welcome to this very sketchy game of chopsticks (hopefully).

Go google or something if you don't know the rules.
              """)
        for i in range(self.player):
            self.add_player(Player(self.hand, i+1))
        
        while(not self.check_win()):
            for player in self.players:
                self.display(player.index)
                player.move()
                if self.check_win():
                    break
    def check_win(self):
        alive_players = []
        for player in self.players:
            if player.is_alive():
                alive_players.append(player.get_index())
        if len(alive_players) == 1:
            print("Player {} wins!".format(alive_players[0]))
            return True
        return False
    
    def add_player(self, player):
        self.players.append(player)
    
    def display(self, index):
        print(f'Player {index}\'s turn: ')
        print("Hand numbers:\t", end='')
        for hand in self.hands:
            print(hand.index, end='\t')
        print()
        print("Hand fingers:\t", end='')
        for hand in self.hands:
            print(hand.fingers, end='\t')
        print()
        
class Player: # hands, 
    def __init__(self, hand, index):
        self.index = index
        self.hand = hand
        self.hands = []
        for i in range(self.hand):
            self.add_hand(i+1)
    
    
    def move(self):
        print(f'Player {self.index}\'s turn: ')
        print("Hand numbers:\t", end='')
        for hand in self.hands:
            print(hand.index, end='\t')
        print()
        print("Hand fingers:\t", end='')
        for hand in self.hands:
            print(hand.fingers, end='\t')
        print()
        
        while True:
            try:
                source = int(input(f"Player {self.index}, which hand do you want to add from: "))
                target = int(input(f"Player {self.index}, which hand do you want to add to: "))
                break
            except ValueError:
                print("Bad input try again :")
            
         
        
    
    def add_hand(self, index):
        self.hands.append(Hand(index))
    
    def get_index(self):
        return self.index
    
    def is_alive(self):
        for hand in self.hands:
            if not hand.is_alive():
                return False
        return True
            
        

class Hand: #fingers
    def __init__(self, index):
        self.fingers = 1
        self.alive = True
        self.index = index
    
    def is_alive(self):
        return self.alive
    
    def check_dead(self):
        if self.fingers > 5:
            self.fingers = 0
            self.alive = False
    

if __name__ == "__main__":
    game = Game(2, 2)
    game.run()
    