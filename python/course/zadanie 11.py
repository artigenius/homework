#Tamagotchi to take care of
class Cat ():
    """ description of tamagotchi """
    def __init__(self, name, health):
        """traits of tamagotchi"""
        self.name = name
        self.health = health
        self.alive = True
        #self.health = 0

    def feed(self, foodCount):
        """feed a cat"""
        self.health = self.health + foodCount
        return ("Cat is fed", 1)

    def punish(self, hit):
        """punish a cat"""
        self.health = self.health - hit
        return ("Cat is punished", 1)


    def run(self):
        if self.health >= 1:
            self.alive = True
        else:
            self.alive = False

    def status(self):
        print(
        f"""
        Name: {self.name}
        Health: {self.health}
        Status: {self.alive}
        """
        )


import random

def main():
    """the main game"""
    print("enter START to begin")
    s=str(input())
    if s != 'start':
        return 0

    print("Let's give a name to our pet!")
    nam = input()
    cat = Cat(nam, random.randint(10,100))
    print("Your cat name is ", cat.name, " his health is at ", cat.health, " HP")
    print("You can Feed your cat: print 'feed, 5 (or any amount of food)"
          "You can Punish you cat: print 'punish, 1 (or any amount of hits)"
          "To know the HP of your cat, is it alive or not, print 'status'")

    com = ' '
    count = 0

    while com:
        print("give a command")
        com, count = input().split()
        com = str(com)
        count = int(count)
        if com == 'feed':
            cat.feed(count)
            print("your cat ", cat.name, " is at ", cat.health, " HP")
        elif com == 'punish':
            cat.punish(count)
            print("your cat ", cat.name, " is at ", cat.health, " HP")
        elif com == 'status':
            cat.status()
        else :
            return 0



main()