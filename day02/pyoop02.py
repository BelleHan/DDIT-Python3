class Dog:
    def __init__(self):
        self.flag_bark = True
        print("constructor")
        
    def train(self):
        self.flag_bark = False
    
    def __del__(self):
        print("destroyer")
    
if True:   
    d = Dog()
    print(d.flag_bark)
    d.train()
    print(d.flag_bark)   
    
print("hello")