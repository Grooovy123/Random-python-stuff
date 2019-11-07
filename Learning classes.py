import time
import random

class Robot:
    def __init__(self, name, weight):        
        self.name = name        
        self.weight = weight        
        
    def introduce_self(self):
        print("my name is " + self.name)        
        
    def bot_colour(self):
        print(self.name + " is " + self.colour)

    def bot_data(self):
        print("your data:")
        print("  your name is " + self.name)        
        print("  you currently weigh " + str(self.weight) + "kg\n")

class env(): #gym
    def __init__(self, cardio=None):
        self.cardio = cardio
        
                
    def cardio_fitness(self,bot):
        bot.weight-=self.cardio
        print(bot.weight)

    def weights(self,bot):
        pass

##gym = env()
##gym.cardio_fitness(bot)
##
##bot = Robot("Granny", "Red", 90)
##bot.bot_data()

def main():
    print("Welcome to gym simulator\n")
    choice = input("Do you want to 1)sign up or 2)sign in : ")
    while choice!= "1" or "2":        
        if choice == "1":
            pass
        elif choice == "2":
            sign_in()
        else:
            print("Thats not a valid option")            
            choice = input("Do you want to 1)sign up or 2)sign in : ")
            
def sign_up():
    pass

def sign_in():
    character_setup()

def character_setup():
    
    print("what name do you want your character to have?")
    character_name = input()

    print("How much do you want your character to start off weighing in kg (30-160kg)\nor type random ")
    weight_done = False
    while weight_done != True:
        weight = input()
        try:                        
            weight = int(weight)
            weight_done = True
        except:
            if weight.lower() == "random":
                weight = random.randint(30,161)
                weight_done = True
            
    Bot1 = Robot(character_name, weight) 
    Bot1.bot_data()
    
main()
    
        
        
        




