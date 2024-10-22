# asking username
username = input ("please enter usernmae: ")

# Display the entered username
print (f"Welcome:{username}")
# asking if user likes superheroes
likes_superheroes =input("do you like superheroes? (yes/no): ").strip().lower()

# Respond based of users input
if likes_superheroes =="yes":
    print("ahh yes someone with class I see")
elif likes_superheroes =="no":
    print("alrigt well why are you here leave :|") 
    sys.exit() #exit program