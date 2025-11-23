class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
        
    def hello(self):
        print("Hello, my name is", self.name)
        
    def googbye(self):
        print("Goodbye, my name is", self.name)
        
m =Man("John")
m.hello()
m.googbye()