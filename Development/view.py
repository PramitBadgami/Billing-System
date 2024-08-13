def display_costume():
    print("\n")
    print("Let's rent a costume.")
    print("\n")

def display_invalidinput():
    print("\n")
    print("++"*20)
    print("Please provide a valid costume ID!!!")
    print("++"*20)
    print("\n")

def show_costumes():
    print("------------------------------------------------------------")
    print("  ID    Custome Name    Custome Brand    Price    Quantity")
    print("------------------------------------------------------------")
    
    file = open("main_text.txt","r")
    List = []
    line = file.readlines()
        
    file.close()
    for i in range(len(List)):
        ListD.append(List[i].split(","))
    print(line)
    
    
