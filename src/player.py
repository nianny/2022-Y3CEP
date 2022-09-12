class OutOfRangeException (Exception):
    pass

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
    
    def print_hands(self, name, first = True):
        if first:
            print(f"{' '*(len(name))}", end='')
            for i in range(len(self.hands)):
                print(i+1, end='\t')
            print()
            print()
        print(f'{name}', end='')
        for i in range(len(self.hands)):
            print(self.hands[i], end='\t')
        print()
        
    def int_input(self, message, min_value, max_value):
        while True:
            try:
                output = int(input(message))
                if output < min_value or output > max_value:
                    raise OutOfRangeException()
                return output
            except OutOfRangeException as e:
                print(f"Out of range. Please input a number between {min_value} and {max_value}.")
            
    
    
    def move(self, board, player):
        print()
        print()
        print(f"Player {player+1}'s turn:")
        # board[player].print_hands(f'Your hand: ')
        for i in range(len(board)):
            
            # input stuff (whether the current display is the first one, since it also has to display header)
            if i == 0:
                first = True
            else:
                first = False
                
                
            if i == player:
                string = "Your hand: "
                board[i].print_hands(string + ' ' * (11 - len(string)), first)
            else:
                string = f'Player {i+1}: '
                board[i].print_hands(string + ' ' * (11 - len(string)), first)
                
                
        #choice of hand input
        while True:
            try:
                hand = int(input("Which hand do you want to add with: "))
                break
            except:
                print("Invalid input.")
        hand = self.int_input(f'Which hand do you want to add with: ', 1, len(board[i].hands))-1
        
        # if there are more than two players, you have to specify which player you want to add toe
        if len(board) > 2:
            
            # since i put it in a function, its quite abit more complicated to add another condition (i think)
            while True:
                target = self.int_input(f'Which player do you want to add to: ', 1, len(board))-1
                if target == player:
                    print("You can't add to yourself.")
                    continue
                break
        else:
            target = (player+1)%2
        
        target_hand = self.int_input(f'Which hand do you want to add to: ', 1, len(board[target].hands))-1
        
        return hand, target, target_hand
        
        
