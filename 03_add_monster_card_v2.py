"""Add Monster Card v2
Second version fixes the informal language and adds more interactive features
while adding an f string to improve complexity
"""


# Add a new monster card to the catalogue
def add_monster_card(catalogue):
    while True:
        # Get monster card name
        monster_card_name = input("Hello! Please enter the monster's name: ")

        # Initialize a dictionary to hold the attributes
        attributes = {}

        # Get values for Strength, Speed, Stealth, and Cunning,
        # ensuring they are within the allowed range
        for attribute in ["Strength", "Speed", "Stealth", "Cunning"]:
            while True:
                try:
                    value = int(
                        input(f"Enter the value for {attribute} (1-25): "))
                    if 1 <= value <= 25:
                        attributes[attribute] = value
                        break
                    else:
                        print("Please enter a value between 1 and 25.")
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")

        # Display the monster card details
        print("\nNew Monster Card Details:")
        print(f"Name: {monster_card_name}")
        for key, value in attributes.items():
            print(f"{key}: {value}")

        # Confirm the details with the user
        is_correct = input("Is this information correct? (yes/no): ").lower()
        if is_correct == 'yes':
            catalogue[monster_card_name] = attributes
            print(f"Congratulations! {monster_card_name} has been added"
                  f" to the catalogue!")
            break
        else:
            print("Okay, let's try entering the monster card details again!")


# Example usage:
monster_card_catalogue = {}
add_monster_card(monster_card_catalogue)
print("\nCurrent Monster Catalogue:")
print(monster_card_catalogue)