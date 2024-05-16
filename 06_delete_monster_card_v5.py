"""Delete Monster Card v5
Fixed error of printing statements without easygui,
as well as printing out the edited catalogue in one
print before exiting program
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


# Function to display the edited monster card catalogue
def show_catalogue(catalogue):
    catalogue_message = ""
    for monster, attributes in catalogue.items():
        catalogue_message += f"{monster}:\n"
        for attr in attributes:
            catalogue_message += f"  {attr[0]}: {attr[1]}\n"
        catalogue_message += "\n"
    easygui.msgbox(catalogue_message, title="Edited Monster Card Catalogue")


# Function to delete monster card from the catalogue using Easygui
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
                show_catalogue(catalogue)
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
                    show_catalogue(catalogue)
                    return
            else:
                easygui.msgbox("User cancelled the deletion. "
                               "Returning to the selection.")


# Example usage
delete_monster_card(monster_catalogue)
