import random 
class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self,name):
        self.name=name 
        self.health = 110
        self.attack_power = 25

    def attack(self):
        """return a random value from 1 through this hero's attack power"""
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        """Subtracts damage from the health but doesn't let health fall below 0"""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Returns a boolean to say whether the hero is alive or not."""
        return self.health > 0
