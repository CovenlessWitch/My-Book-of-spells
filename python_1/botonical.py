import sys

def superhero_interaction():
    SPIDERMAN = "spiderman"
    BATMAN = "batman"
    favorite_superheroes = []  # List to store favorite superheroes
    
    # Asking for username
    username = input("Hello, please enter a username: ")
    
    # Display welcome message with user name
    print(f"Welcome {username}")

    # Asking if user likes superheroes
    while True:
        likes_superheroes = input("Do you like superheroes? (yes/no): ").strip().lower()
        
        # Respond based on user input
        if likes_superheroes == "yes":
            print("Ahh yes, you're a person of high class I see 🥴")
            
            # Ask for favorite superheroes
            while True:
                favorite = input("What's your favorite superhero? (type 'done' when finished): ").strip().lower()
                if favorite == 'done':
                    break
                favorite_superheroes.append(favorite)

            while True:
                spiderman_vs_batman = input(f"Who wins, base {SPIDERMAN} or base {BATMAN}? ({SPIDERMAN}/{BATMAN}): ").strip().lower()
                
                # Responses based on user input
                if spiderman_vs_batman == SPIDERMAN:
                    print("Oh yeah this guy's invited to the cookout!")
                    break  # Exit inner loop after giving a thank you message
                elif spiderman_vs_batman == BATMAN:
                    print("Yeah, and how much PREP TIME did he need? 😒 Well, whatever, thanks for your input I guess...")
                    break  # Exit inner loop after giving a thank you message
                else:
                    print(f"Please answer with '{SPIDERMAN}' or '{BATMAN}'.")

            # Thank you message after exiting the inner loop
            print("fyi I love Batman; I just think Spiderman beats him in a head-on fight. Don't go all fan on me 🙄")
            break  # Exit outer loop after user interaction
        
        elif likes_superheroes == "no":
            print("Alright, well why are you here then... leave 😐")
            print("Thanks for stopping by!")
            sys.exit()  # Remove user from the program
        
        else:
            print("Please answer 'yes' or 'no'.")

    # Display the list of favorite superheroes
    if favorite_superheroes:
        print(f"Your favorite superheroes are: {', '.join(favorite_superheroes)}")
    else:
        print("You didn't list any favorite superheroes.")

# Call the function to run the interaction
superhero_interaction()
