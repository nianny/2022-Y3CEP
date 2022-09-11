class GameOptions:
    def __init__(self, default_value, description):
        self.value = default_value  
        self.explaination = description
        
    def list(self, pos):
        print(f"{pos}. {self.explaination}", end='\t')

class ToggleGameOptions (GameOptions):
    def __init__(self, default_value, description):
        super().__init__(default_value, description)

    def edit(self):
        self.value = not self.value
        return self.value

    def list(self, pos):
        super().list(pos)
        if self.value:
            print("Yes")
        else:
            print("No")
        
class NumGameOptions (GameOptions):
    def __init__(self, default_value, description, min_value, max_value, query_string):
        super().__init__(default_value, description)
        self.min_value = min_value
        self.max_value = max_value
        self.query_string = query_string
    
    def edit(self):
        while True:
            try:
                self.value = int(input(f"{self.query_string} (between {self.min_value} and {self.max_value}): "))
                if not (self.value >= self.min_value and self.value <= self.max_value):
                    raise Exception("Invalid input")
                break
            except:
                print("Invalid input.\n")   
    
    def list(self, pos):
        super().list(pos)
        print(self.value)   