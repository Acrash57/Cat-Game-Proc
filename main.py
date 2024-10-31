import time 
cat_attributes = {
    "intelligence": 50,
    "energy": 5,
    "weight": 5,
}

print("Welcome to my cat game!") 
name = input("Enter the name of your cat: ")
colour = input("What is its colour: ")

while True:
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats 4. Let your cat sleep: 5. Feed your cat: ")

    if option == '1' and cat_attributes["energy"] > 0:
        print("Your cat has played!")
        cat_attributes["energy"] -= 1
        cat_attributes["weight"] -= 0.1
    elif option == '2':
        print("Your cat has trained!")
        cat_attributes["intelligence"] += 1
    elif option == '3':
        print(f"{name}'s Attributes")
        for x in cat_attributes:
            print(f"{x} = {cat_attributes[x]}")
    elif option =='4':
        print("Your cat has taken a nap!")
        cat_attributes["energy"] += 2 
    elif option == '5':
        print("Your cat has eaten!")
        cat_attributes["weight"] += 0.1 

    if cat_attributes['energy'] == 0:
        print("Your cat is very tired it cannot play again, you might want to let it sleep")
        time.sleep(1.5)
    if cat_attributes["weight"] < 3.5: 
        print(f"{name} is severely underweight and has passed away :(")
        time.sleep(1.5) 
        print("Maybe it wasn't a good idea to overwork your cat")
        quit()
    if cat_attributes["weight"] > 6.5: 
        print(f"{name} is severely overweight and has passed away :(")
        time.sleep(1.5)
        print("Maybe it wasn't a great idea to overfeed your cat")
        quit() 
