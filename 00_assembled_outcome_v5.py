"""Assembled Outcome v5
Finished Outcome, edited to meet all PEP8 Requirements
"""
from easygui import buttonbox, \
    msgbox, ynbox, enterbox, choicebox, integerbox, multenterbox

# Storing Monster Card Details
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


# Function to allow the user to add a new monster card
def add_monster_card(catalogue):
    fields = ["Name", "Strength", "Speed", "Stealth", "Cunning"]
    while True:
        inputs = multenterbox(
            "Hello! Please enter the details for the new monster card:\n "
            "(The Strength, Speed, Stealth, Cunning, must be between 1-25):",
            "New Monster Card", fields)

        if inputs is None:
            break

        monster_card_name, strength, speed, stealth, cunning = inputs

        try:
            strength, speed, stealth, cunning = int(strength), int(speed), \
                int(stealth), int(cunning)
            if not all(1 <= x <= 25 for x in [strength, speed, stealth,
                                              cunning]):
                msgbox(
                    "All attributes must be between 1 and 25. "
                    "Please try again.",
                    "Invalid Input.")
                continue
        except ValueError:
            msgbox(
                "Please enter valid numbers for attributes. Please try again.",
                "Invalid Input")
            continue

        details = f"Name: {monster_card_name}\nStrength: {strength}\nSpeed: " \
                  f"{speed}\nStealth: {stealth}\nCunning: {cunning}"
        if ynbox(f"Is this information correct?\nNew monster card details:"
                 f"\n{details}", "New Monster Card", ["Yes", "No"]):
            catalogue[monster_card_name] = [
                ["Strength", strength],
                ["Speed", speed],
                ["Stealth", stealth],
                ["Cunning", cunning]
            ]
            msgbox("Monster card added successfully!", "Success!")
            break
        else:
            if not ynbox("Do you want to re-enter the details?", "Retry",
                         ["Yes", "No"]):
                break


# Function to allow the user to search for an existing monster card
def search_monster_card():
    while True:
        monster_choices = list(monster_catalogue.keys())
        monster_choices.append("Cancel")
        choice_ = buttonbox("Choose a monster card to view its details:",
                            choices=monster_choices,
                            title="Search Existing Monster Card")
        if choice_ == "Cancel":
            break
        elif choice_:
            details = ""
            for attribute in monster_catalogue[choice_]:
                details += f"{attribute[0]}: {attribute[1]}\n"
            msgbox(details, title=choice + " Details")
        else:
            break


def edit_monster_card():
    while True:
        monster_names = list(monster_catalogue.keys())
        if not monster_names:
            msgbox("No monster cards available to edit.", "Empty Catalogue")
            break

        # Choosing a monster to edit
        monster_name = choicebox("Select a monster card to edit:",
                                 "Edit Monster Card", monster_names)
        if monster_name is None:
            break  # User cancelled the operation

        new_monster_name = enterbox("Enter new name for the monster card:",
                                    "Edit Monster Name", monster_name)
        if new_monster_name is not None and new_monster_name != "":
            monster_catalogue[new_monster_name] = \
                monster_catalogue.pop(monster_name)
            monster_name = new_monster_name

        # Finding the selected monster's attributes
        selected_monster = monster_catalogue[monster_name]

        while True:
            attribute_names = [attribute[0] for attribute in selected_monster]
            attribute_to_edit = choicebox(f"Select an attribute of "
                                          f"{monster_name} to edit:\n\n" 
                                          f"{selected_monster}",
                                          "Select Attribute", attribute_names)
            if attribute_to_edit is None:
                break  # User cancelled the operation

            for attribute in selected_monster:
                if attribute[0] == attribute_to_edit:
                    new_value = integerbox(f"Enter new value for "
                                           f"{attribute_to_edit} "
                                           f"(1-25):", title="Edit Attribute",
                                           lowerbound=1, upperbound=25)
                    if new_value is not None:
                        attribute[1] = new_value
                        msgbox(f"{attribute_to_edit} updated to {new_value}"
                               f" for {monster_name}.",
                               "Attribute Updated")

            # Check if the user wants to continue editing
            if not ynbox("Do you want to continue editing this monster card?",
                         "Continue Editing?",
                         ["Yes", "No"]):
                break


# Function to delete monster card from the catalogue using Easygui
def delete_monster_card(catalogue):
    while True:
        if not catalogue:
            msgbox("No monster cards left in the catalogue.",
                   "Catalogue Empty")
            break

        while True:
            monster_names = list(catalogue.keys())
            monster_names.append("Cancel")
            choice_ = buttonbox("Select a monster card to delete or Cancel to "
                                "exit:",
                                "Delete Monster Card",
                                choices=monster_names)

            if choice_ == "Cancel":
                return

            monster_details = catalogue[choice_]
            details_message = f"Name: {choice_}\n" + "\n".join([f"{attr[0]}: "
                                                               f"{attr[1]}" for
                                                                attr in
                                                                monster_details
                                                                ])
            confirm_delete = ynbox(f"Are you sure you want to delete "
                                   f"this monster card?\n"
                                   f"{details_message}",
                                   "Confirm Delete")
            # If the user confirms deletion
            if confirm_delete:
                del catalogue[choice_]
                msgbox(f"Monster card '{choice_}' has been deleted.",
                       "Deleted Successfully!")
                if not ynbox("Do you want to delete more monster "
                             "cards?", "Continue Deleting?",
                             ["Yes", "No"]):
                    return
            else:
                msgbox("User cancelled the deletion. "
                       "Returning to the selection.")


# Function to print the monster card catalogue
def print_catalogue():
    output = "𝓜𝓸𝓷𝓼𝓽𝓮𝓻 𝓒𝓪𝓻𝓭 𝓒𝓪𝓽𝓪𝓵𝓸𝓰:\n\n"

    for monster, attributes in monster_catalogue.items():
        output += f"🐉 𝓜𝓸𝓷𝓼𝓽𝓮𝓻: {monster} 🐲\n"
        for attr, value in attributes:
            output += f"• {attr}: {value}"
        output += "\n\n"

    msgbox(output, "𝓜𝓸𝓷𝓼𝓽𝓮𝓻 𝓒𝓪𝓻𝓭 𝓒𝓪𝓽𝓪𝓵𝓸𝓰")


# Main loop
while True:
    message = "\n*** Welcome! What would you like to do today? ***\n" \
              "                                 Options:"
    title = "Monster Catalogue"
    choices = [
        "Add New Monster Card",
        "Search Existing Monster Card",
        "Edit Monster Card",
        "Delete Monster Card",
        "Print Monster Catalogue",
        "Exit Program"
    ]

    choice = buttonbox(message, title=title, choices=choices)

    if choice == "Add New Monster Card":
        add_monster_card(monster_catalogue)
    elif choice == "Search Existing Monster Card":
        search_monster_card()
    elif choice == "Edit Monster Card":
        edit_monster_card()
    elif choice == "Delete Monster Card":
        delete_monster_card(monster_catalogue)
    elif choice == "Print Monster Catalogue":
        print_catalogue()
    elif choice == "Exit Program":
        msgbox("Thank you for using this program! Farewell!",
               title="Farewell, User!")
        break
    else:
        break
