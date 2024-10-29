import sys

def superhero_interaction():
    """
    This function interacts with the user to discuss their preferences for superheroes,
    collects their favorite superheroes, and provides a fun debate between Spiderman and Batman.
    """
    # Asking for username
    user_name = input("Hello, please enter a username: ")
    
    # Display welcome message with user name
    print(f"Welcome {user_name}")

    # Asking if the user likes superheroes
    while True:
        likes_superheroes_response = input("Do you like superheroes? (yes/no): ").strip().lower()
        
        # Respond based on user input
        if likes_superheroes_response == "yes":
            print("Ahh yes, you're a person of high class I see 🥴")
            
            # Collect favorite superheroes in a list
            favorite_superheroes = []  # List to store favorite superheroes
            
            while True:
                favorite_superhero = input("What's your favorite superhero? (type 'done' when finished): ").strip().lower()
                if favorite_superhero == 'done':
                    break
                favorite_superheroes.append(favorite_superhero)

            # Ask who wins in a matchup
            while True:
                superhero_matchup = input("Who wins, base Spiderman or base Batman? (spiderman/batman): ").strip().lower()
                
                # Responses based on user input
                if superhero_matchup == "spiderman":
                    print("Oh yeah, this guy's invited to the cookout!")
                    break  # Exit inner loop after giving a thank you message
                elif superhero_matchup == "batman":
                    print("Yeah, and how much PREP TIME did he need? 😒 Well, whatever, thanks for your input I guess...")
                    break  # Exit inner loop after giving a thank you message
                else:
                    print("Please answer with 'spiderman' or 'batman'.")

            # Thank you message after exiting the inner loop
            print("FYI, I love Batman; I just think Spiderman beats him in a head-on fight. Don't go all fan on me 🙄")
            break  # Exit outer loop after user interaction
        
        elif likes_superheroes_response == "no":
            print("Alright, well why are you here then... leave 😐")
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
