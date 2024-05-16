"""Delete Monster Card v2
Allows the user to delete monster cards from the
catalogue using an enterbox"""
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


# Trial 2 = Using an Easygui Enterbox
def show_monster_details(catalogue, monster_name):
    if monster_name in catalogue:
        details = catalogue[monster_name]
        details_message = f"Monster: {monster_name}\n"
        for attr in details:
            details_message += f"{attr[0]}: {attr[1]}\n"
        return easygui.ynbox(details_message, title="Monster Card Details",
                             choices=["Delete", "Cancel"])
    else:
        easygui.msgbox("Monster card not found in the catalogue.",
                       title="Error")
        return False


# Get the monster card name from the user
monster_name = easygui.enterbox("Enter the name of the monster card to "
                                "delete: ", title="Monster Card Deletion")

# Double check if the user wants to delete the entered monster card
confirmation = show_monster_details(monster_catalogue, monster_name)

if confirmation:
    del monster_catalogue[monster_name]
    easygui.msgbox(f"The monster card '{monster_name}' has been deleted.",
                   title="Deleted Successfully")
else:
    easygui.msgbox("Deletion cancelled. The monster card has not been deleted."
                   "", title="Deletion Cancelled")
