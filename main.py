class Person:
    def __init__(self, name, age, city):
        self.name = name  # Имя
        self.age = age    # Возраст
        self.city = city  # Город

    # Метод introduce для представления информации о человеке
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")

    # Метод is_adult для проверки совершеннолетия
    def is_adult(self):
        return self.age >= 18  # Возвращаем True, если возраст >= 18

    # Переопределение метода __str__ для удобного строкового представления
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"


# Создание экземпляров класса Person
person1 = Person(name="John", age=25, city="New York")
person2 = Person(name="Alice", age=17, city="Los Angeles")

# Вызов метода introduce для каждого экземпляра
person1.introduce()  # Привет, меня зовут John, мне 25 лет, я живу в New York
person2.introduce()  # Привет, меня зовут Alice, мне 17 лет, я живу в Los Angeles

# Проверка совершеннолетия с помощью метода is_adult
print(f"Is {person1.name} an adult? {person1.is_adult()}")  # True
print(f"Is {person2.name} an adult? {person2.is_adult()}")  # False

# Вывод экземпляров класса, используя __str__()
print(person1)  # Имя: John, Возраст: 25, Город: New York
print(person2)  # Имя: Alice, Возраст: 17, Город: Los Angeles
