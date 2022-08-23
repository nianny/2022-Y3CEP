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
        
        toggle = True
        while(toggle):
            for player in self.players:
                self.display(player.index)
                self.move(player)
                if self.check_win():
                    toggle = False
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
        for player in self.players:
            player.display()
    
    def move(self, player):
        while True:
            try:
                source = int(input(f"Player {player.index}, which hand do you want to add from: "))
                if source < 1 or source > self.hand or not player.has_hand(source):
                    raise ValueError("Invalid source hand")
                
                if self.player > 2:
                    target_player = int(input(f"Player {player.index}, which player do you want to add to: "))
                    if target_player < 1 or target_player > self.player:
                        raise ValueError("Invalid target player")
                else:
                    target_player = player.index%2 + 1
                
                target_hand = int(input(f"Player {player.index}, which hand do you want to add to: "))
                if target_hand < 1 or target_hand > self.hand or not self.players[target_player-1].has_hand(target_hand):
                    raise ValueError("Invalid target hand")
                print()
                break
            except ValueError:
                print("Bad input try again:")
        
        self.players[target_player-1].add_to_hand(player.get_fingers(source), target_hand)
        
    
    
        
class Player: # hands, 
    def __init__(self, hand, index):
        self.index = index
        self.hand = hand
        self.hands = []
        for i in range(self.hand):
            self.add_hand(i+1)
    
    def display(self):
        print(f'Player {self.index}: ')
        print("Hand numbers:\t", end='')
        for hand in self.hands:
            print(hand.index, end='\t')
        print()
        print("Hand fingers:\t", end='')
        for hand in self.hands:
            if hand.is_alive():
                print(hand.fingers, end='\t')
            else:
                print("X", end='\t')
        print()  

    def has_hand(self, hand):
        return self.hands[hand-1].is_alive()
    
    def add_hand(self, index):
        self.hands.append(Hand(index))
    
    def get_index(self):
        return self.index
    
    def is_alive(self):
        for hand in self.hands:
            if hand.is_alive():
                return True
        return False

    def get_fingers(self, hand):
        return self.hands[hand-1].get_fingers()

    def add_to_hand(self, fingers, hand):
        self.hands[hand-1].add_fingers(fingers)
        self.hands[hand-1].check_dead()


class Hand: #fingers
    def __init__(self, index):
        self.fingers = 1
        self.alive = True
        self.index = index
    
    def is_alive(self):
        return self.alive
    
    def check_dead(self):
        if self.fingers >= 5:
            self.fingers = 0
            self.alive = False
    
    def get_fingers(self):
        return self.fingers
    
    def add_fingers(self, fingers):
        self.fingers += fingers
    

if __name__ == "__main__":
    game = Game(2, 2)
    game.run()
    