### 🧙‍♂️ Defeat the Evil Wizard - Python Battle Game
## Overview
Welcome to the Defeat the Evil Wizard turn-based battle game! In this Python project, players create a hero character and engage in combat against the Evil Wizard using Object-Oriented Programming (OOP) principles. Players can attack, heal, and use special abilities to emerge victorious in battle.

## Features ✨
- Playable Characters: Choose from Warrior, Mage, Archer, or Paladin, each with unique attributes.

- Special Abilities: Each character has two special abilities that can enhance combat.

- Turn-Based Combat: Players and the Evil Wizard take turns selecting actions.

- Healing Mechanic: Characters can heal but cannot exceed their maximum health.

- Randomized Attacks: Attack power varies dynamically within a set range.

- Enemy AI: The Evil Wizard regenerates health and retaliates.

## Object-Oriented Structure 🛠️
The game is designed using OOP principles:

# Base Character Class
```bash
python
class Character:
    def __init__(self, name, health, attack_power):
Encapsulates common properties such as name, health, and attack_power.
```

Defines attack, heal, and display_stats methods.

# Character Subclasses
Each playable character is a subclass of Character, inheriting its properties and methods while adding unique abilities.

# Warrior ⚔️
```bash
python
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
```
Special Ability 1: Rage (double attack)

Special Ability 2: Swift Feet (dodge next attack)

# Mage 🔥
```bash
python
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=25)
```
Special Ability 1: Greater Fire Ball (inflict bonus damage)

Special Ability 2: Magic Mirror (block next attack)

# Archer 🏹
```bash
python
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
```
Special Ability 1: Double Arrow Attack (shoot twice)

Special Ability 2: Evade (dodge next attack)

# Paladin 🛡️
```bash
python
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
```
Special Ability 1: Divine Strike (double attack)

Special Ability 2: Divine Shield (block next attack)

# Evil Wizard Class
```bash
python
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=175, attack_power=15)
```
Regenerates health each turn.

Attacks the player after their turn.

# Gameplay 🕹️
Start the game and choose a character class.

Engage in turn-based combat against the Evil Wizard.

Choose from Attack, Special Ability, Heal, or View Stats.

Defeat the wizard or be defeated!

# Running the Game 🚀
To play, simply run:

```bash
python battle_game.py
```
Make sure you have Python installed.

# Future Enhancements 🌟
- Additional characters with unique mechanics.

- More advanced AI behavior for the wizard.

- A graphical user interface (GUI) for better interactivity.

Enjoy battling the Evil Wizard! ⚡