import os
class Player: 
    """Creates player for the Survival Game."""
    
    def __init__(self):
        
        """ 
        Sets the initial amount of wood, food, fire, knife durability,
        and health the player has on its first day. 
        
        """
        self.name = ""
        self.wood = 0
        self.food = 0
        self.fire = 0
        self.knife_dur = 0
        self.health = 0
        
    def set_name(self,name):
        
        """Allows player to choose his/her name."""
        
        self.name = name

    def build_fire(self):
        
        """
        Loses 5 damage points to the amount of wood the player has
        and gains 2 points to the amount of fire the player has. 
        
        """
        self.wood -= 5
        self.fire += 2

    def eat_food(self):
        
        """Loses 1 damage point to the amount of food the player has."""
        
        self.food -= 1

    def find_food(self):
    
        """
        Checks if player has enough knife durability to find food.
        
        Knife durability takes 1 damage point to the total amount of 
        knife durability the player has when finding food,
        but adds 1 point to the amount of food the player has.
        
        """
        
        if self.check_knife(1):
            self.knife_dur -= 1
            self.food += 1

    def find_wood(self):

        """
        Checks if player has enough knife durability to find wood.  
        
        Knife durability takes 3 damage points to the total amount of 
        knife durability the player has when finding wood,
        but adds 5 points to the amount of wood the player has
        
        """
        if self.check_knife(3):
            self.knife_dur -= 3
            self.wood += 5

    def check_knife(self, dmg):

        """Notifies the player that knife durability is 0"""
        
        if self.knife_dur - dmg < 0:
            print("Your knife is as dull as my soul.")
            return False
        else:
            return True  
        
class SurvivalGame:
    
    """Creates the 7 days of a survival game. Takes inputs 1-5 of player's choice."""
    
    def __init__(self):
        
        """
        Sets initial amount of player's health and knife durability. Starts off the game
        with counting down the days, starting at 7. Player has not eaten anything at the
        beginning of the game.
        
        """
        
        self.player = Player()
        self.player.health = 50
        self.player.knife_dur = 7
        self.days = 7
        self.ate_food = False
    
    def start(self):
        
        """
        Starts the game by asking the player's name, allowing the player to type 
        his/her name. Checks if player has health points and days remaining to continue
        the game. Provides options for survival to choose tasks wisely in order to survive 
        for 7 days. 
        
        """
        name = input("What's your name?") 
        self.player.name = name
        output = ""

        while self.player.health > 0 and self.days > 0:
            ate_food = False
            os.system('clear')
            self.print_player()
            print("\n" + output + "\n")
            output = ""
            print("What do you want to do?")
            choice = input("""1: Eat some food
2: Find some wood
3: Build a fire
4: Find some food 
5: Nothing (just die)""")
            if choice == '1':
                if self.player.food > 0:
                    self.player.eat_food()
                    output += "That was delicious"
                    self.ate_food = True
                else:
                    output += "You have no food! Sucks you can't eat."
                    
            elif choice == '2':
                    self.player.find_wood()
                    output += "Ya found some wood."
                    
            elif choice == '3':
                if self.player.wood > 4:
                    self.player.build_fire()
                    output += "I feel toasty"
                else: 
                    output += "You don't have wood. I guess you're just going to freeze to death."
                    
            elif choice == '4':
                self.player.find_food()
                output += "You're not going to starve."
            
            elif choice == '5':
                self.player.health = 0

            else:
            	output += "Can't you follow instructions, you wasted a day you fool."
                
            self.check_status(self.ate_food)
            self.new_day()
            self.endgame()
            
    
    def check_status(self, ate_food):
        
        """Checks if player has eaten or not."""
        
        dmg = 0
        if self.player.fire > 0:
            self.player.fire -= 1
        else:
            dmg += 5
        
        if not ate_food:
            dmg += 5

        self.player.health -= dmg
        dmg = 0

    def new_day(self):
        
        """Creates a new day."""
        
        self.ate_food = False 
        self.days -= 1
    
    def endgame(self):
        
        """
        
        Determines the result of the survival game. If player makes it through 7 days with 
        health points remaining, the player has succeeded in making it alive. Game ends if 
        player's health reaches 0 within the week. 
        
        """
        
        if self.days == 0:
            print("Good job you made it alive")
        elif self.player.health <= 0:
        	print("YA DED")
        elif self.days > 0:
            print("Another day, another chance to live")
        else:
            print("Sorry you died")
    
    def print_player(self):
        
        """
        
        Shows the status of the player's health, resources, and how many days remaining,
        so player is able to choose what to do next in order to make it out alive.
        
        """
        
        print("""\
Status of {0}
health: {health}
wood: {1}
fire: {2}
food: {3}
knife durability: {4}
Day {5}""".format(self.player.name,
                  self.player.wood,
                  self.player.fire,
                  self.player.food,
                  self.player.knife_dur,
                  self.days,health = self.player.health))
            