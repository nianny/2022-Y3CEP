class OutOfRangeException (Exception):
    pass

class InvalidHand (Exception):
    pass

class InvalidPlayer(Exception):
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
                hand = int(input("Which hand do you want to tap with: "))
                
                # hand pos out of range
                if hand < 1 or hand > len(board[player].hands):
                    raise OutOfRangeException()
                
                hand -= 1 #since hand data is 0 indexed while input is 1 indexed
                
                # you cannot add with an already "dead" hand
                if board[player].hands[hand] == 0:
                    raise InvalidHand()
                break
            
            except OutOfRangeException:
                print(f"Invalid input. Number has to be between 1 and {len(board[player].hands)}.") 
                print()
            except InvalidHand:
                print("You cannot tap with a hand that is dead!")
                print()
            except:
                print("Invalid input.")
                print()
                
        
        
        # input for which person to tap on
        while True:
            try:
                target = int(input("Which player do you want to tap: "))
                if target < 1 or target > len(board): #out of range for players
                    raise OutOfRangeException()
                
                target -= 1 #since target data is 0 indexed while input is 1 indexed
                
                #dead player cannot be tapped on (although only applies, hopefully, when there is more than 2 players)
                if not board[target].check_alive(): 
                    raise InvalidPlayer()
                break
            
            except InvalidPlayer:
                print(f"Invalid input. Player {target+1} is already dead.")
                print()
            except OutOfRangeException:
                print(f"Invalid input. Number has to be between 1 and {len(board)}.")
                print()
            except:
                print("Invalid input.")
                print()
                
            
            
        while True:
            try:
                target_hand = int(input("Which hand do you want to tap: "))
                
                # hand pos out of range
                if target_hand < 1 or target_hand > len(board[target].hands):
                    raise OutOfRangeException()
                
                target_hand -= 1 #since hand data is 0 indexed while input is 1 indexed
                
                # you cannot add with an already "dead" hand
                if board[target].hands[target_hand] == 0:
                    raise InvalidHand()
                if player == target and target_hand == hand:
                    raise InvalidHand()
                break
            
            except OutOfRangeException:
                print(f"Invalid input. Number has to be between 1 and {len(board[target].hands)}.") 
                print()
            except InvalidHand:
                print("Invalid input. Either this hand is dead or you are tapping on the same hand!")
                print()
            except:
                print("Invalid input.")
                print()
                
        print()
        return hand, target, target_hand
        
        
