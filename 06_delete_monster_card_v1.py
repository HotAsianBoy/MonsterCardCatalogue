"""Delete Monster Card v1
Allows the user to delete an existing monster
card from the catalogue using a buttonbox
"""
import easygui
# Storing Monster Details
monster_catalogue = {
    "Stoneling": [
        ["Strength", 7],
        ["Speed", 1],
        ["Stealth", 25],
        ["Cunning", 15],
    ],
    "Vexscream": [
        ["Strength", 1],
        ["Speed", 6],
        ["Stealth", 21],
        ["Cunning", 19],
    ],
    "Dawnmirage": [
        ["Strength", 5],
        ["Speed", 15],
        ["Stealth", 18],
        ["Cunning", 22]
    ],
    "Blazegolem": [
        ["Strength", 15],
        ["Speed", 20],
        ["Stealth", 23],
        ["Cunning", 6]
    ],
    "Websnake": [
        ["Strength", 7],
        ["Speed", 15],
        ["Stealth", 10],
        ["Cunning", 5]
    ],
    "Moldvine": [
        ["Strength", 21],
        ["Speed", 18],
        ["Stealth", 14],
        ["Cunning", 5]
    ],
    "Vortexwing": [
        ["Strength", 19],
        ["Speed", 13],
        ["Stealth", 19],
        ["Cunning", 2]
    ],
    "Rotthing": [
        ["Strength", 16],
        ["Speed", 7],
        ["Stealth", 4],
        ["Cunning", 12]
    ],
    "Froststep": [
        ["Strength", 14],
        ["Speed", 14],
        ["Stealth", 17],
        ["Cunning", 4]
    ],
    "Wispghoul": [
        ["Strength", 17],
        ["Speed", 19],
        ["Stealth", 3],
        ["Cunning", 2]
    ]
}


# Trial 1 = Using an Easygui Buttonbox
def delete_monster_card(catalogue):
    while True:
        if not catalogue:
            easygui.msgbox("No monster cards left in the catalogue.",
                           "Catalogue Empty")
            break

        monster_names = list(catalogue.keys())
        monster_names.append("Cancel")
        choice = easygui.buttonbox("Select a monster card to delete or "
                                   "Cancel to exit:",
                                   "Delete Monster Card",
                                   choices=monster_names)

        if choice == "Cancel":
            print("Final catalogue before exiting:")
            print_catalogue(catalogue)
            break

        monster_details = catalogue[choice]
        details_message = f"Name: {choice}\n" + "\n".join([f"{attr[0]}: "
                                                           f"{attr[1]}" for
                                                           attr in
                                                           monster_details])
        confirm_delete = easygui.ynbox(f"Are you sure you want to delete this "
                                       f"monster card?\n{details_message}",
                                       "Confirm Delete")
        # If user confirms the deletion
        if confirm_delete:
            del catalogue[choice]
            easygui.msgbox(f"Monster card '{choice}' has been deleted.",
                           "Deleted Successfully")
            if not easygui.ynbox("Do you want to delete more monster cards?",
                                 "Continue Deleting?", ["Yes", "No"]):
                print("Final catalogue after deletions:")
                print_catalogue(catalogue)
                break
        else:
            print("User cancelled the deletion. Current catalogue:")
            print_catalogue(catalogue)
            break


# Function to print out the catalogue before exiting program
def print_catalogue(catalogue):
    for monster, attributes in catalogue.items():
        print(f"{monster}:")
        for attr in attributes:
            print(f"  {attr[0]}: {attr[1]}")
        print()


# Example usage
delete_monster_card(monster_catalogue)