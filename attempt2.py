class Minimax:
    def __init__(self):
        pass
    
    def run(self, board, player):
        pass
    
    def check_win(self, board, player):
        
        alive_counter = 0
        for player in board:
            if player.check_alive():
                alive_counter += 1
        
        
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
    def __init__(self, hand_number):
        self.hands = [1]*hand_number
    
    def check_hand(self):
        for hand in self.hands:
            if hand >= 5:
                hand = 0
    
    def check_alive (self):
        self.check_hand()
        for hand in self.hands:
            if hand > 0:
                return True
        return False
    
board = [Player(2), Player(2)]
print(board[0].check_alive())
# print(minimax(board, 1))