class Minimax:
    store = {}
    def __init__(self):
        pass
    
    # player 0 maximises, player 1 minimises
    def run(self, board, player, hist = []):
        if len(board) > 2:
            raise Exception("Board size too large")
        
        opponent = (player+1)%2
        if self.check_end(board, hist):
            print(board[0].hands, board[1].hands, self.check_win(board, hist), hist)
            return self.check_win(board, hist)

        
        lis = []
        for hand in range(len(board[player].hands)):
            for target in range(len(board[opponent].hands)):
                if board[opponent].hands[target] == 0 or board[player].hands[hand] == 0:
                    continue
                replica = board.copy()
                replica[opponent].hands[target] += board[player].hands[hand]
                replica[opponent].check_hand()
                print(hand, target, replica, board)
                lis.append((self.run(replica, opponent, hist + [board]), hand, target))
        
        lis.sort(reverse = True)
        print(lis)
        if player == 0:
            return lis[0][1], lis[0][2]
        else:
            return lis[-1][1], lis[-1][2]
                
            

    def check_end(self, board, hist):
        alive_counter = 0
        for player in board:
            if player.check_alive():
                alive_counter += 1
        
        if alive_counter == 1 or board in hist:
            return True
        else:
            return False
            
    def check_win(self, board, hist):
        if board in hist:
            return 0.5
        elif board[0].check_alive() and not board[1].check_alive():
            return 1
        elif board[1].check_alive() and not board[0].check_alive():
            return 0
            
             
            
        
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

mini = Minimax()
board = [Player(hand = [1,4]), Player(hand = [1,0])]
# print(board)
dead = Player(hand= [0,0])
print(dead.check_alive())
print(mini.run(board, 0))
# print(minimax(board, 1))