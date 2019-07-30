class Car :
    def __init__(self,name) :
        self.name = name
        
print(globals()['Car'])
c = globals()['Car']("Ford")
print(c.name)