import sys

def superhero_interaction():
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

            # Ask another question
            spiderman_vs_batman = input("Who wins, base Spiderman or base Batman? (spiderman/batman): ").strip().lower()
            
            # Responses based on user input
            if spiderman_vs_batman == "spiderman":
                print("Oh yeah this guys invited to the cookout!")
                break # Exit loop after giving a thank you message
            elif spiderman_vs_batman == "batman":
                print("Yeah, and how much PREP TIME did he need? 😒 Well, whatever, thanks for your input!")
                break  # Exit loop after giving a thank you message
            else:
                print("Please answer with 'spiderman' or 'batman'.")
        
        elif likes_superheroes == "no":
            print("Alright, well why are you here then... leave 😐")
            sys.exit()  # Remove user from the program
        
        else:
            print("Please answer 'yes' or 'no'.")  

    # Thank you message after exiting the loop
    print("fyi i love batman i just thinks spiderman beats him in a head on fight")

# Call the function to run the interaction
superhero_interaction()
