from player import Player

class Minimax (Player):
    # store = {}
    def __init__(self, hand_number = 2, hand = None):
        super().__init__(hand_number, hand)
    
    # player 0 maximises, player 1 minimises
    def run(self, board, player, hist = []):
        if len(board) > 2:
            raise Exception("Board size too large")

        # tupled = []
        # for player in board:
        #     tupled.append(tuple(player.hands))
        # tupled = tuple(tupled)

        # if (player, tupled) in store:
        #     return store[(player, tupled)]
        
        opponent = (player+1)%2
        if self.check_end(board, hist):
            return (self.check_win(board, hist),0,0)

        
        lis = []
        for hand in range(len(board[player].hands)):
            for target in range(len(board[opponent].hands)):
                if board[opponent].hands[target] == 0 or board[player].hands[hand] == 0:
                    continue
                replica = []
                for p in board:
                    replica.append(p.copy())
                replica[opponent].hands[target] += replica[player].hands[hand]
                replica[opponent].check_hand()
                lis.append((False, self.run(replica, opponent, hist + [board])[1], hand, target))
        
        #taking into consideration splits
        possi = [[0]*len(board[player].hands)]
        for i in range(sum(board[player].hands)):
            new_possi = []
            for pos in possi:
                for p in range(len(pos)):
                    dup = pos.copy()
                    dup[p] += 1
                    new_possi.append(dup)
            possi = new_possi
        
        print(possi)
            
            
        lis.sort(reverse = True)
        
        
        # tupled = []
        # for player in board:
        #     tupled.append(tuple(player.hands))
        # tupled = tuple(tupled)
        # store[(0, tupled)] = lis[0]
        # store[(1, tupled)] = lis[-1]
        
        if player == 0:
            return lis[0]
        else:
            return lis[-1]
                
            

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
    
    def move(self, board, player):
        output = self.run(board, player)
        
        return output[0], output[2], (player+1)%2, output[3]