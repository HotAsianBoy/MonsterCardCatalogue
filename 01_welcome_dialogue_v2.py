"""Welcome Dialogue v2
Added easygui to the program, which will allow
the user to make the needs required simpler
and easier
"""
import easygui

# Main loop
while True:
    message = "\n*** Welcome What would you like to do today? ***\nOptions:"
    title = "Monster Catalogue"
    choices = [
        "Add New Monster Card",
        "Search Existing Monster Card",
        "Delete Monster Card",
        "Edit Monster Card",
        "Print Monster Catalogue",
        "Exit Program"
    ]

    choice = buttonbox(message, title=title, choices=choices)

    if choice == "Add New Monster Card":
        add_monster_card(monster_catalogue)
    elif choice == "Search Existing Monster Card":
        search_monster_card()
    elif choice == "Delete Monster Card":
        delete_monster_card(monster_catalogue)
    elif choice == "Edit Monster Card":
        edit_monster_card(monster_catalogue)
    elif choice == "Print Monster Catalogue":
        print_catalogue()
    elif choice == "Exit Program":
        print("Exiting program.")
        break
    else:
        break

