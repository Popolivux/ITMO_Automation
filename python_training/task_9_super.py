class A:
    def __init__(self):
        self.x = 10




class B(A):
    def __init__(self):
        super().__init__()      #если в сбоках после __init__
        self.y = self.x + 5

print(B().y) # лучше сначала присваивать значение, потом вызывать класс

b = B()
print(b.y)