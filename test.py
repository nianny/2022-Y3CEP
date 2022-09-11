class Test:
    def __init__(self):
        self.hallo = 1
    
    def __repr__(self) -> str:
        return str(self.hallo)
    
    def copy(self):
        return Test()

# list1 = [Test()]
# print(list1)
# list2 = list1.copy()
# print(list2)
# list2[0].hallo = 2
# print(list1, list2)

t = Test()
t2 = t.copy()
print(t, t2)
t.hallo = 2
print(t, t2)