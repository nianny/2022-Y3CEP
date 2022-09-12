class Test:
    def __init__(self):
        self.hallo = 1
    
    def __repr__(self) -> str:
        return str(self.hallo)
    
    def copy(self):
        return Test()

class Test1 (Test):
    def __init__(self):
        super().__init__()


test = Test()
test1 = Test1()
print(test)
print(test1)
print(test1.copy())