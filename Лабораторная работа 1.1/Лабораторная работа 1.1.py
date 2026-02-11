
from abc import ABC, abstractmethod


class Furniture(ABC):
    def __init__(self, material: str, dimensions: tuple):
        """
        Конструктор класса Furniture.

        :param material: Материал, из которого изготовлена мебель. Должен быть строкой.
        :param dimensions: Размеры мебели в формате (ширина, высота, глубина).
                           Должны быть положительными числами.

        :raises ValueError: Если материал не строка или размеры некорректны.
        """
        if not isinstance(material, str):
            raise ValueError("Material must be a string.")
        if not all(isinstance(dimension, (int, float)) and dimension > 0 for dimension in dimensions):
            raise ValueError("Dimensions must be positive numbers.")

        self.material = material
        self.dimensions = dimensions

    @abstractmethod
    def assemble(self) -> None:
        """Метод для сборки мебели."""
        pass

    @abstractmethod
    def disassemble(self) -> None:
        """Метод для разборки мебели."""
        pass


class Chair(Furniture):
    def assemble(self) -> None:
        """Собрать стул."""
        print(f"Assembling a chair made of {self.material} with dimensions {self.dimensions}.")

    def disassemble(self) -> None:
        """Разобрать стул."""
        print("Disassembling the chair.")


class Tree(ABC):
    def __init__(self, species: str, age: int):
        """
        Конструктор класса Tree.

        :param species: Вид дерева. Должен быть строкой.
        :param age: Возраст дерева в годах. Должен быть положительным целым числом.

        :raises ValueError: Если вид не строка или возраст не положительное целое число.
        """
        if not isinstance(species, str):
            raise ValueError("Species must be a string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        self.species = species
        self.age = age

    @abstractmethod
    def grow(self) -> None:
        """Метод для роста дерева."""
        pass

    @abstractmethod
    def shed_leaves(self) -> None:
        """Метод для сбрасывания листьев."""
        pass


class Oak(Tree):
    def grow(self) -> None:
        """Дерево растет."""
        print(f"The {self.species} tree is growing.")

    def shed_leaves(self) -> None:
        """Дерево сбрасывает листья."""
        print(f"The {self.species} tree is shedding its leaves.")


class SocialMedia(ABC):
    def __init__(self, name: str, user_count: int):
        """
        Конструктор класса SocialMedia.

        :param name: Название социальной сети. Должен быть строкой.
        :param user_count: Количество пользователей. Должно быть положительным целым числом.

        :raises ValueError: Если название не строка или количество пользователей не положительное целое число.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(user_count, int) or user_count <= 0:
            raise ValueError("User count must be a positive integer.")

        self.name = name
        self.user_count = user_count

    @abstractmethod
    def post_update(self, content: str) -> None:
        """Метод для публикации обновления."""
        pass

    @abstractmethod
    def analyze_trends(self) -> dict:
        """Метод для анализа трендов."""
        pass


class Facebook(SocialMedia):
    def post_update(self, content: str) -> None:
        """Опубликовать обновление на Facebook."""
        print(f"Posting update on {self.name}: {content}")

    def analyze_trends(self) -> dict:
        """Анализировать тренды на Facebook."""
        return {"trend": "example trend"}


if __name__ == "__main__":
    # Пример использования классов
    chair = Chair("wood", (50, 100, 50))
    chair.assemble()
    chair.disassemble()

    oak_tree = Oak("oak", 100)
    oak_tree.grow()
    oak_tree.shed_leaves()

    facebook = Facebook("Facebook", 2900000000)
    facebook.post_update("Hello, world!")
    trends = facebook.analyze_trends()
    print(trends)
