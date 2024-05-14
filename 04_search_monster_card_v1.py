"""Search Monster Card v1
Asks the user the name of the monster card to search using
and easygui enterbox
"""
import easygui
# Storing Monster Details
monster_name = {
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


# Trial 1 = Using Easygui Enterbox
def search_monster_card(catalogue):
    while True:
        search_query = easygui.enterbox("Enter the name of the monster card "
                                        "you want to search for:",
                                        "Search Monster Card")
        if search_query is None:
            return  # User cancelled the search

        # Normalize the search query to improve match chances
        search_query = search_query.strip().lower()
        found = False

        for monster_name, attributes in catalogue.items():
            if monster_name.lower() == search_query:
                details_message = f"Name: {monster_name}\n"
                details_message += "\n".join([f"{key}: {value}" for key,
                value in attributes.items()])
                easygui.msgbox(details_message, "Monster Card Details:")
                found = True
                break

        if not found:
            if easygui.ynbox("Monster card not found. Would you like "
                             "to search again?", "Not Found", ["Yes", "No"]):
                continue
            else:
                break


# Example usage
monster_catalogue = {}
search_monster_card(monster_catalogue)
