class Animal:
    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация базового класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self.__name = name  # Инкапсуляция, чтобы защитить имя от изменения извне
        self.__age = age    # Инкапсуляция, чтобы защитить возраст от изменения извне

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Animal."""
        return f"{self.__class__.__name__}(Name: {self.__name}, Age: {self.__age})"

    def __repr__(self) -> str:
        """Возвращает неформальное строковое представление объекта Animal."""
        return f"{self.__class__.__name__}(name={self.__name!r}, age={self.__age!r})"

    def make_sound(self) -> str:
        """Издает звук животного. Метод может быть переопределен в дочерних классах."""
        return "Some sound"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.breed = breed  # Порода собаки

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Dog."""
        return f"{super().__str__()}, Breed: {self.breed}"

    def make_sound(self) -> str:
        """Издает звук собаки. Переопределение метода для специфичного поведения."""
        return "Woof!"

    def fetch(self) -> str:
        """Метод, который позволяет собаке приносить предметы."""
        return f"{self.breed} is fetching the ball!"


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Инициализация класса Cat.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.color = color  # Цвет кошки

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Cat."""
        return f"{super().__str__()}, Color: {self.color}"

    def make_sound(self) -> str:
        """Издает звук кошки. Переопределение метода для специфичного поведения."""
        return "Meow!"

    def scratch(self) -> str:
        """Метод, который позволяет кошке царапать предметы."""
        return f"{self.color} cat is scratching the furniture!"


if __name__ == "__main__":
    dog = Dog(name="Rex", age=5, breed="German Shepherd")
    cat = Cat(name="Whiskers", age=3, color="Tabby")

    print(dog)  # Выводит строковое представление собаки
    print(cat)  # Выводит строковое представление кошки

    print(dog.make_sound())  # Выводит звук собаки
    print(cat.make_sound())  # Выводит звук кошки

    print(dog.fetch())  # Выводит действие собаки
    print(cat.scratch())  # Выводит действие кошки

