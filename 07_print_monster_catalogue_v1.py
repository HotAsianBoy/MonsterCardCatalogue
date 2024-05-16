"""Print Monster Catalogue v1
Allows the user to print the monster catalogue
"""

import easygui

monster_card_list = {
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


def print_catalogue():
    output = "🐲 𝕸𝖔𝖓𝖘𝖙𝖊𝖗 𝕮𝖆𝖗𝖉 𝕮𝖆𝖙𝖆𝖑𝖔𝖌 🐉\n\n"

    for monster, attributes in monster_card_list.items():
        output += f"🔸 {monster} 🔸\n"
        for attribute in attributes:
            output += f"• {attribute[0]}: {attribute[1]}\n"
        output += "\n"

    easygui.buttonbox(output, "🐉 𝕸𝖔𝖓𝖘𝖙𝖊𝖗 𝕮𝖆𝖗𝖉 𝕮𝖆𝖙𝖆𝖑𝖔𝖌 🐲", choices=["OK"])


print_catalogue()
