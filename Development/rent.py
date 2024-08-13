print("\n\nLet's rent a costume\n\n")
text = open('main_text.txt', 'r')        
text_list = text.readlines()                  
text_list_list = []                                  
for i in range(len(text_list)):
    text_list_list.append(text_list[i].split(","))

    print("***********************************************************************")
    print("  ID\t\tCostume\t\tBrand\t\tPrice\t\tStock")
    print("***********************************************************************")
for i in range(len(text_list)):
    print("|",text_list_list[i][0],"\t\t",text_list_list[i][1],"\t",text_list_list[i][2],"\t",text_list_list[i][3],"\t\t",text_list_list[i][4],"  |")
    print("***********************************************************************")

user_in = int(input("Enter the ID of the dress you want: "))     
got = False                                                
for i in range(len(text_list_list)):
    if user_in == int(text_list_list[i][0]):
        print("\n\n We got the costume\n\n")
        user_in_quantity = int(input("Enter the quantity: "))        
        if user_in_quantity > int(text_list_list[user_in][4]):
            print("Quantity out of range!!!!!!!!")
            rent()
        else:
            text_list_list[user_in][4] = int(text_list_list[user_in][4]) - user_in_quantity
            print("\n\nRENTED!!\n\n")
            got = True
            break
 
    if got == False:

        print("\n\n Enter valis ID!!!\n\n")

    print(text_list_list)

    main()
