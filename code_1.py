class Animal:
    
    def Eat(self):
        print("The animal eats")

class Mammal(Animal):
    def breast_feed(self):
        print("The animal breastfeeds.")

class Ave(Animal):
    def Fly(self):
        print("The animal flies")
    
class Bat(Mammal, Ave):
    pass


bat = Bat()

bat.Fly()
bat.Eat()
bat.breast_feed()

print(Bat.mro())
    