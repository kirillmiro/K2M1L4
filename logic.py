from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.base_experience = self.get_base_experience()
        self.cries = self.get_cries()
        self.hp = randint(50, 500) 
        self.power = randint(10, 100)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/shiny/572.gif"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_base_experience(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['base_experience'])
        else:
            return 50
        
    def get_cries(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['cries']['latest'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/572.ogg"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name} \n Базовый опыт твоего покеомона:{self.base_experience} \n Здоровье твоего покеомона:{self.hp} \n Сила твоего покеомона:{self.power}"

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return f"Покемон волшебник применил щит в сражении."
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
class Wizard(Pokemon):
    def info(self):
        return f"У тебя покемон волшебник: \n\n" + super().info()
    
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        результат = super().attack(enemy)
        self.power -= super_power
        return результат + f"\nБоец применил супер-атаку силой:{super_power} "
    def info(self):
        return f"У тебя покемон боец: \n\n" + super().info()
    

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
