import pandas as pd

# Define new dictionary from TS Mapping

hero_role_mapping = {
    "Ana": "Support",
    "Ashe": "Damage",
    "Baptiste": "Support",
    "Bastion": "Damage",
    "Brigitte": "Support",
    "Cassidy": "Damage",
    "Doomfist": "Tank",
    "D.Va": "Tank",
    "Echo": "Damage",
    "Genji": "Damage",
    "Hanzo": "Damage",
    "Illari": "Support",
    "Junker Queen": "Tank",
    "Junkrat": "Damage",
    "Kiriko": "Support",
    "Lifeweaver": "Support",
    "Lúcio": "Support",
    "Mauga": "Tank",
    "Mei": "Damage",
    "Mercy": "Support",
    "Moira": "Support",
    "Orisa": "Tank",
    "Pharah": "Damage",
    "Ramattra": "Tank",
    "Reaper": "Damage",
    "Reinhardt": "Tank",
    "Roadhog": "Tank",
    "Sigma": "Tank",
    "Sojourn": "Damage",
    "Soldier: 76": "Damage",
    "Sombra": "Damage",
    "Symmetra": "Damage",
    "Torbjörn": "Damage",
    "Tracer": "Damage",
    "Widowmaker": "Damage",
    "Winston": "Tank",
    "Wrecking Ball": "Tank",
    "Zarya": "Tank",
    "Zenyatta": "Support",
}

# Convert dict to df
heroes = pd.DataFrame(list(hero_role_mapping.items()), columns=['Hero', 'Role'])
