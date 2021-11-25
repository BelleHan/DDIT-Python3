class Animal:
    def __init__(self):
        self.age = 0
    def getOlder(self):
        self.age+=1
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill = 0
    def use(self,skill):
        self.skill += skill

        
hum = Human()
print(hum.age)
print(hum.skill)
hum.getOlder()
hum.use(7)
print(hum.age)
print(hum.skill)

