class Weapon:
    bullets = 0

    def __init__(self, bullets: int):
        self.bullets = bullets
        Weapon.bullets = self.bullets

    def shoot(self):
        while Weapon.bullets > 0:
            Weapon.bullets -= 1
            return "shooting..."

        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {Weapon.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
