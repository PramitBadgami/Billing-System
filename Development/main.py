import rent
print("++"*25)
print("       Welcome to costume rental application")
print("++"*25,"\n\n")

def main():
    while True:
        print("Select a desirable option")
        print("(1) || Press 1 to rent a costume.")
        print("(2) || Press 2 to return a costume.")
        print("(3) || Press 3 to exit.")
        user = int(input("Enter a option: "))
        if user == 1:
            view.display_costume()
            view.show_costumes()
        elif user == 2:
            print("\nLet's return a costume.\n")
        elif user == 3:
            print("\n        Thank You for using our application.")
            break
        else:
            print("\nInvalid input!!!!")
            print("Please select the value as per the provided options.\n")
main()
