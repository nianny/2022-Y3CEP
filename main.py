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
        
    def check_win(self):
        alive_players = []
        for player in self.players:
            if player.is_alive():
                alive_players.append(player.get_index())
        
    
    def add_player(self, player):
        self.players.append(player)
    
class Player: # hands, 
    def __init__(self, hand, index):
        self.index = index
        self.hand = hand
        self.hands = []
        for i in range(self.hand):
            self.add_hand()
    
    
    def add_hand(self):
        self.hands.append(Hand())
    
    def get_index(self):
        return self.index
            
        

class Hand: #fingers
    def __init__(self):
        pass
    

if __name__ == "__main__":
    game = Game(2, 2)
    game.run()
    