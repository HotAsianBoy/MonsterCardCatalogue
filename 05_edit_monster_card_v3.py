"""Edit Monster Card v3
Added the values of the attributes of monster card
before being edited to improve usability, and to check if the
changes are saved
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


# Function to edit a monster card using EASYGUI
while True:
    monster_names = list(monster_catalogue.keys())
    if not monster_names:
        easygui.msgbox("No monster cards available to edit.",
                       "Empty Catalogue")
        break

    # Choosing a monster to edit
    monster_name = easygui.choicebox("Select a monster card to edit:",
                                     "Edit Monster Card", monster_names)
    if monster_name is None:
        break  # User cancelled the operation

    new_monster_name = easygui.enterbox("Enter new name for the monster card:"
                                        "", "Edit Monster Name", monster_name)
    if new_monster_name is not None and new_monster_name != "":
        monster_catalogue[new_monster_name] = \
            monster_catalogue.pop(monster_name)
        monster_name = new_monster_name

    # Finding the selected monster's attributes
    selected_monster = monster_catalogue[monster_name]

    while True:
        attribute_names = [attribute[0] for attribute in selected_monster]
        attribute_to_edit = easygui.choicebox(f"Select an attribute of "
                                              f"{monster_name} to edit:\n\n"
                                              f"{selected_monster}",
                                              "Select Attribute",
                                              attribute_names)
        if attribute_to_edit is None:
            break  # User cancelled the operation

        for attribute in selected_monster:
            if attribute[0] == attribute_to_edit:
                new_value = easygui.integerbox(f"Enter new value for "
                                               f"{attribute_to_edit} (1-25):",
                                               title="Edit Attribute",
                                               lowerbound=1, upperbound=25)
                if new_value is not None:
                    attribute[1] = new_value
                    easygui.msgbox(f"{attribute_to_edit} updated to "
                                   f"{new_value}"
                                   f" for {monster_name}.",
                                   "Attribute Updated")

        # Check if the user wants to continue editing
        if not easygui.ynbox("Do you want to continue editing this "
                             "monster card?", "Continue Editing?",
                             ["Yes", "No"]):
            break
