name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input (
    "You are on top of a mountain with a wooden bridge in front of you, do you want to cross or walk around? Type 'cross' or 'walk around': ").lower()

if answer == "cross":
    answer = input(
        "After crossing the bridge, you continue to walk along a dirt road, until you come across a bear by surprise. Do you fight him or run away? Type 'fight' or 'run': ").lower()
    if answer == "fight":
        print("You were the bear's lunch :(. ")
        
    elif answer == "run":
        answer = input(
            "You run many miles and find a family. Do you talk with them(Yes/No)? ").lower()
        if answer == "yes":
            print("They help you and you won.")
            
        elif answer == "no":
            print("You die.")
            
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")



elif answer == "walk around":
    answer = input("After walking around you come across a tribe, you have the option to interact with them or continue walking. Type 'interact' or 'continue': ").lower()
    if answer == "interact":
        print('The tribe thinks you are the enemy and they tie you to a fire. You lose.')
    elif answer == "continue":
        print('You run out of water and supplies and you die. ')
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")
    
print("Thank you and Goodbye.")
