"""Add Monster Card v5
Added an easygui multi-box to simplify the use of the code for the user
"""
import easygui


def add_new_monster_card(catalogue):
    fields = ["Name", "Strength", "Speed", "Stealth", "Cunning"]
    while True:
        # Use multenterbox to get all inputs at once
        inputs = easygui.multenterbox(
            "Hello! Please enter the details for the new monster card\n "
            "(The Strength, Speed, Stealth, Cunning, must be between 1-25):",
            "New Monster Card", fields)

        # Check if the user cancelled the operation
        if inputs is None:
            break

        # Unpack inputs
        monster_card_name, strength, speed, stealth, cunning = inputs

        # Validate numeric inputs
        try:
            strength, speed, stealth, cunning = int(strength), int(speed), int(
                stealth), int(cunning)
            if not all(
                    1 <= x <= 25 for x in [strength, speed, stealth, cunning]):
                easygui.msgbox(
                    "All attributes must be between 1 and 25. "
                    "Please try again.",
                    "Invalid Input.")
                continue
        except ValueError:
            easygui.msgbox(
                "Please enter valid numbers for attributes. Please try again.",
                "Invalid Input")
            continue

        # Confirm monster card details
        details = f"Name: {monster_card_name}\nStrength: {strength}\nSpeed:" \
                  f" {speed}\nStealth: {stealth}\nCunning: {cunning}"
        if easygui.ynbox(f"Is this information correct?\n"
                         f"New monster card details:\n{details}",
                         "New Monster Card", ["Yes", "No"]):
            # Add to catalogue if confirmed
            catalogue[monster_card_name] = {
                "Strength": strength,
                "Speed": speed,
                "Stealth": stealth,
                "Cunning": cunning
            }
            easygui.msgbox("Monster card added successfully!", "Success!")
            break
        else:
            if not easygui.ynbox("Do you want to re-enter the details?",
                                 "Retry", ["Yes", "No"]):
                break


# Example usage
monster_catalogue = {}
add_new_monster_card(monster_catalogue)
easygui.msgbox(f"Current Monster Catalogue:\n{monster_catalogue}",
               title="Monster Catalogue")