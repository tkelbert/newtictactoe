print("---defining the pet class")

class Pet:
    def __init__(self, pet_name):
        print(f"DEBUG: initializing new pet named {pet_name}")

        ##attribiutes (use self to creat attributes from this specific object)
        self.name = pet_name
        self.hunger = 50
        self.boredom = 50
        self.rage = 50
        self.attack = False
        print(f"DEBUG: {self.name} created with {self.hunger} hunger, {self.boredom} boredom, and {self.rage} rage")

    def check_status(self):
        print(f"\n----{self.name}'s status ---")
        print(f" Hunger: {self.hunger}")
        print(f" Boredom: {self.boredom}")
        print(f" Rage: {self.rage}")
    
    def feed(self):
        print(f"\Feeding with {self.name}")
        self.hunger -= 15

        if self.hunger < 0:
            self.hunger = 0
            print("you are full")
        
        print(f"{self.name} says yum!")
        print(f"(hunger is now: {self.hunger})")

    def play(self):
        print(f"\nYou play with {self.name}")
        self.boredom -= 10
        if self.boredom < 0:
            self.boredom = 0
        
        print(f"{self.name} is happy to play!")
        print(f"({self.name}'s boredom level is now: {self.boredom})")

    def annoy(self):
        print(f"\nYou try to annoy {self.name}")
        self.rage += 10
        if self.rage >99:
            print("Te la mamaste")
            print(f"{self.name} becomes enraged and attacks you")
            self.attack = True
        print(f"you pissed {self.name} off. his rage level is {self.rage}")

    def handle_unknown(self, command):
        print(f"{command} is not a recognized command")

    def attacks(self):
        print(f"you have gone too far {self.name} attacks you")
        self.rage -= 10
        print(f"she feels better after attacking you")


print("---Pet class defined---")


pet= Pet(pet_name="michele")
running = True

print(f"you have a new pet named {pet.name}")

while running:
    pet.check_status()
    command = input("What do you want to do? (feed/play/annoy/quit) > ")

    if command == "feed":
        pet.feed()
    elif command == "play":
        pet.play()
    elif command == "annoy":
        pet.annoy()
        if pet.attack == True:
            pet.attacks()
            
    elif command == "quit":
        running = False
    else:
        pet.handle_unknown(command)