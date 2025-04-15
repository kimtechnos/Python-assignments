# Smartphone base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand                       # Public attribute
        self._model = model                      # Protected attribute (by convention)
        self.__battery_life = battery_life       # Private attribute in hours

    def introduce(self):
        print(f"This is a {self.brand} {self._model} with battery life of {self.__battery_life} hours.")

    def use(self):
        print(f"Using {self.brand} {self._model} for basic tasks...")

    # Getter for private attribute
    def get_battery_life(self):
        return self.__battery_life

    # Setter for private attribute
    def set_battery_life(self, new_life):
        if new_life >= 0:
            self.__battery_life = new_life
        else:
            print("Battery life cannot be negative!")
# Subclass representing a gaming smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu_power):
        super().__init__(brand, model, battery_life)
        self.gpu_power = gpu_power  # Additional attribute for gaming phone

    # Overriding the use method to demonstrate polymorphism
    def use(self):
        print(f"Gaming on {self.brand} {self._model} with GPU power of {self.gpu_power}!")

    def show_specs(self):
        print(f"{self.brand} {self._model} Specs:")
        print(f"Battery Life: {self.get_battery_life()} hours")
        print(f"GPU Power: {self.gpu_power}")

phone1 = Smartphone("Samsung", "A52", 20)
phone1.introduce()
phone1.use()
phone1.set_battery_life(4)
print("Updated battery life:", phone1.get_battery_life())
print()

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 24, "Adreno 730")
gaming_phone.introduce()
gaming_phone.use()  # Polymorphism in action!
gaming_phone.show_specs()
