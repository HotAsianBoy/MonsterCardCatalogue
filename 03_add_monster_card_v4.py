"""Add Monster Card v4
Fixed printing each stat (attribute) in a separate box and prints the
full details into one box, as well as fixing saving the monster details
if the information is correct"""
import easygui


def add_new_monster_card(catalogue):
    while True:
        # Get monster card name
        monster_card_name = easygui.enterbox("Hello! Please enter the "
                                             "monster's name:",
                                        title="New Monster Card")

        # Initialize a dictionary to hold the attributes
        attributes = {}
        valid_input = True

        # Get values for Strength, Speed, Stealth, and Cunning,
        # ensuring they are within the allowed range
        for attribute in ["Strength", "Speed", "Stealth", "Cunning"]:
            value = easygui.integerbox(
                f"Please enter the value for {attribute} (1-25):", lowerbound=1,
                upperbound=25, title="Attribute Input")
            if value is None:
                valid_input = False
                break
            attributes[attribute] = value

        if not valid_input:
            continue

        # Display the monster card details
        details = f"Monster Card Name: {monster_card_name}\n"
        details += "\n".join(
            [f"{key}: {value}" for key, value in attributes.items()])
        easygui.msgbox(details, title="New Monster Card Details")

        # Confirm the details with the user
        is_correct = easygui.buttonbox("Is this information correct?",
                                   choices=["Yes", "No"])
        if is_correct:
            catalogue[monster_card_name] = attributes
            easygui.msgbox("Monster card added successfully!"
                           "", title="Success!")
            break
        else:
            easygui.msgbox(
                "Let's try entering the monster card details again!",
                title="Retry")


# Example usage:
monster_catalogue = {}
add_new_monster_card(monster_catalogue)
easygui.msgbox(f"Current Monster Catalogue:\n{monster_catalogue}",
               title="Monster Catalogue")
