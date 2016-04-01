class Character:
    def __init__(self,name,initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    def __str__(self):
        s = "Name : " + self.name
        s += "  Health : " + str(self.health)
        s += "  Inventory : " + str(self.inventory)
        return s

    def grab(self,item):
        self.inventory.append(item)

    def get_health():
        return self.health
    
def example():
    mychar = Character("Mehdi",50)
    mychar.grab("test")
    print str(mychar)
   # print mychar.name
    #print mychar.health
    #print mychar.inventory

example()
