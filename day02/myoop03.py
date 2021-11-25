class Dog:
    def __init__(self):
        self.flag_bark = True
    def train(self):
        self.flag_bark = False

class Bird:
    def __init__(self):
        self.skill_fly = False
    def gosang(self):
        self.skill_fly = True
        
class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
     
     
if __name__ == "__main__":
    gs = GaeSae()
    print(gs.flag_bark)
    print(gs.skill_fly)
    gs.train()
    gs.gosang()
    print(gs.flag_bark)
    print(gs.skill_fly)
