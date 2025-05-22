# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    # Special Ability: Rage (bonus damage)
    def special1(self):
        pass 
    
    # Special Ability: Swift Feet (dodge attack)
    def special2(self):
        pass 
        

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        
    # Special Ability: Spell Book (extra heal)
    def special1(self): 
        pass 
    
    # Special Ability: Magical Force (blocks attack)
    def special2(self):
        pass 


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=175, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
        
    # Special Ability: Double arrow attack
    def special1(self):
        pass 
    
    # Evade, dodges next attack 
    def special2(self):
        pass 

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        
    # Special Ablility: Holy Strike (bonus damage)
    def special1(self):
        pass 
    
    # Special Ability: Divine Shield (blocks next attack) 
    def special2(self):
        pass 


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name) 
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            pass  # Implement special abilities
            print("\n--- Special Abilities ---") 
            print("1. Damage Boost")
            print("2. Dodge Attack") 
            ability = input("Enter the number of the special ability you wish to use: ")
            if ability == '1':
                player.special1()
            elif ability == '2':
                player.special2()
            else:
                print("Invalid Choice. Try again.")
            
        elif choice == '3':
            pass  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()