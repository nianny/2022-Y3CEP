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
            # print(board[0].hands, board[1].hands, self.check_win(board, hist), hist)
            return (self.check_win(board, hist),0,0)

        
        lis = []
        for hand in range(len(board[player].hands)):
            for target in range(len(board[opponent].hands)):
                if board[opponent].hands[target] == 0 or board[player].hands[hand] == 0:
                    continue
                print(board)    
                replica = []
                for p in board:
                    replica.append(p.copy())
                replica[opponent].hands[target] += replica[player].hands[hand]
                replica[opponent].check_hand()
                print(id(replica), id(board))
                # print(hand, target, replica, board)
                print(board)
                lis.append((self.run(replica, opponent, hist + [board])[0], hand, target))
        print(lis)
        lis.sort(reverse = True)
        print(lis)
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