"""Delete Monster Card v3
Fixes error where if the user doesnt want to detete
any more monster cards, the code prints out
the edited catalogue before
exiting program
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


# Function to print out edited catalogue before exiting program
def print_catalogue(catalogue):
    for monster, attributes in catalogue.items():
        easygui.msgbox(f"{monster}:")
        for attr in attributes:
            easygui.msgbox(f"  {attr[0]}: {attr[1]}")
        easygui.msgbox()


# Function to delete monster card from the catalogue using EASYGUI
def delete_monster_card(catalogue):
    while True:
        if not catalogue:
            easygui.msgbox("No monster cards left in the catalogue.",
                           "Catalogue Empty")
            break

        while True:
            monster_names = list(catalogue.keys())
            monster_names.append("Cancel")
            choice = easygui.buttonbox("Select a monster card to delete or "
                                       "Cancel to exit:",
                                       "Delete Monster Card",
                                       choices=monster_names)

            if choice == "Cancel":
                print("Final catalogue before exiting:")
                print_catalogue(catalogue)
                return

            monster_details = catalogue[choice]
            details_message = f"Name: {choice}\n" + "\n".join([f"{attr[0]}: "
                                                               f"{attr[1]}" for
                                                               attr in
                                                               monster_details]
                                                              )
            confirm_delete = easygui.ynbox(f"Are you sure you want to delete "
                                           f"this monster card?\n"
                                           f"{details_message}",
                                           "Confirm Delete")
            # If the user confirms deletion
            if confirm_delete:
                del catalogue[choice]
                easygui.msgbox(f"Monster card '{choice}' has been deleted.",
                               "Deleted Successfully")
                if not easygui.ynbox("Do you want to delete more monster "
                                     "cards?", "Continue Deleting?",
                                     ["Yes", "No"]):
                    print("Final catalogue after deletions:")
                    print_catalogue(catalogue)
                    return
            else:
                print("User cancelled the deletion. Returning to the "
                      "selection.")


# Example usage
delete_monster_card(monster_catalogue)