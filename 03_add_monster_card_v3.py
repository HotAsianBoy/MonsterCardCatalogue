"""Add Monster Card v3
Third version adds a GUI (Easygui) to the final program which allows
the user to add a new monster card to the catalogue
"""
import easygui

# Add a new monster card to the catalogue
def add_monster_card(catalogue):
    while True:
        # Get monster card name
        monster_card_name = easygui.enterbox("Hello! Please enter the"
                                             " monster's name: ")

        # Initialize a dictionary to hold the attributes
        attributes = {}

        # Get values for Strength, Speed, Stealth, and Cunning,
        # ensuring they are within the allowed range
        for attribute in ["Strength", "Speed", "Stealth", "Cunning"]:
            while True:
                try:
                    value = int(
                        easygui.enterbox(f"Enter the value "
                                         f"for {attribute} (1-25): "))
                    if 1 <= value <= 25:
                        attributes[attribute] = value
                        break
                    else:
                        easygui.msgbox("Please enter a value "
                                       "between 1 and 25.")
                except ValueError:
                    easygui.msgbox("Invalid input. "
                                   "Please enter a numerical value.")

        # Display the monster card details
        easygui.msgbox("\nNew Monster Card Details:\n\n")
        easygui.msgbox(f"Name: {monster_card_name}")
        for key, value in attributes.items():
            easygui.msgbox(f"{key}: {value}")

        # Confirm the details with the user
        is_correct = easygui.buttonbox("Is this information correct?",
                                       choices=["Yes", "No"]).lower()
        if is_correct == 'Yes':
            catalogue[monster_card_name] = attributes
            easygui.msgbox(f"Congratulations!"
                           f" {monster_card_name} has been added "
                  f"to the catalogue!")
            break
        else:
            easygui.msgbox("Okay, let's try entering the "
                           "monster card details again!")


# Example usage:
monster_card_catalogue = {}
add_monster_card(monster_card_catalogue)
easygui.msgbox("\nCurrent Monster Catalogue:")
easygui.msgbox(monster_card_catalogue)