import time
import random
cat_attributes = {
    "intelligence": 50,
    "energy": 5,
    "weight": 5,
}
print("Welcome to my cat game!")



def namecheck(): 
    name = input("Enter the name of your cat: ")
    while name.isnumeric() == True or name == '': 
        name = input("Enter a valid name: ")
    else:
        return name
name = namecheck()

def colourcheck():
    colour = input("What is its colour: ")
    while colour.isnumeric() == True or colour == '':
        colour = input("Enter a valid colour: ")
    else:
        return colour
colour = colourcheck() 



while True:
    option = input("What would you like to do? \n1. Play with your cat \n2. Train your cat \n3. Show stats \n4. Let your cat sleep \n5. Feed your cat: ")

    if option == '1' and cat_attributes["energy"] >= 0:
        print("Your cat has played!")
        time.sleep(1) 
        cat_attributes["energy"] -= 1
        cat_attributes["weight"] -= 0.10
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        if num1 == num2:
            print(f"{name} has hit their head into the table whilst playing")
            time.sleep(1) 
            print(f"{name} has lost some intelligence :(")
            cat_attributes["intelligence"] -= 15
        if cat_attributes["energy"] == 0:
            print("Your cat is very tired it cannot play again, you might want to let it sleep")
            time.sleep(1.5)

    elif option == '2':
        print("Your cat has trained!")
        time.sleep(1) 
        cat_attributes["intelligence"] += 2

    elif option == '3':
        print(f"{name}'s Attributes")
        for x in cat_attributes:
            print(f"{x} = {cat_attributes[x]}")
        time.sleep(1.5)

    elif option =='4':
        print("Your cat has taken a nap!")
        time.sleep(1) 
        cat_attributes["energy"] += 2 

    elif option == '5':
        print("Your cat has eaten!")
        time.sleep(1) 
        cat_attributes["weight"] += 0.20



    if cat_attributes["weight"] < 3.5: 
        print(f"{name} is severely underweight and has passed away :(")
        time.sleep(1.5) 
        print("Maybe it wasn't a good idea to overwork your cat")
        quit()
    if cat_attributes["weight"] > 6.5: 
        print(f"{name} is severely overweight and has passed away :(")
        time.sleep(1.5)
        print(f"Maybe it wasn't a great idea to overfeed {name}")
        quit()
    if cat_attributes["intelligence"] >= 70:
        print(f"{name} has attained high intelligence and found a lost 5 pound note!")
        time.sleep(1) 
        print("Congratulations!")
        time.sleep(1)
    if cat_attributes["intelligence"] <= 30: 
        print(f"{name} has developed cognitive dysfunction syndrome due to low intelligence and got lost outside :(")
        time.sleep(1.5) 
        quit() 
    if cat_attributes["energy"] >= 15:
        print(f"{name} has too much energy it's advised to let {name} play")
        time.sleep(1.5) 

