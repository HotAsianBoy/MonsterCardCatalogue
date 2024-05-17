"""Welcome Dialogue v1
The main loop function for the user's requirements,
each selection will lead to a different function, accoirding
to the user's needs
"""
# Main loop
while True:
    print("\n*** Welcome! What would you like to do today? ***\nOptions:")
    print("****************************************")
    print("1 - Add a new monster card")
    print("2 - Search for an existing monster card")
    print("3 - Delete a monster card")
    print("4 - Edit a monster card")
    print("5 - Print monster catalogue")
    print("6 - Exit Program")
    print("****************************************")
    choice = input("Please choose an option: ")

    if choice == '1':
        add_monster_card()
    elif choice == '2':
        search_monster_card()
    elif choice == '3':
        edit_monster_card()
    elif choice == '4':
        delete_monster_card()
    elif choice == '5':
        print_monster_catalogue()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")