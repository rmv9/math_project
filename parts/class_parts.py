"""The main construct file."""

from functools import singledispatchmethod
from random import randint


class MainExercise:
    """The main exercise class."""

    def __init__(self):
        """Initialize the main exercise class."""
        self.person_1, self.person_2 = self.get_persons_names()
        self.answer = self.get_ans()

    @singledispatchmethod
    def get_random_parameters(self, num_set):
        """Get a random parameters."""
        a, b, c, d = num_set
        return randint(a, b), randint(c, d)

    @get_random_parameters.register(int)
    def int_get_random_parameters(self, a, b, c, d):
        """Get a random parameters."""
        return randint(a, b), randint(c, d) 

    def get_persons_names(self):
        """Get a random persons names."""
        name_1 = (
            "Коля",
            "Вася",
            "Петя",
            "Борис",
            "Егор",
            "Никита",
            "Артур",
            "Стас",
            "Максим",
            "Дима",
            "Витя",
            "Данил",
        )

        name_2 = (
            "Сережа",
            "Саша",
            "Кузя",
            "Андрей",
            "Паша",
            "Семён",
            "Ярослав",
            "Денис",
            "Алексей",
            "Михаил",
            "Артем",
        )

        return (
            name_1[randint(0, len(name_1) - 1)],
            name_2[randint(0, len(name_2) - 1)],
        )

    def get_answer(self):
        pass


class EasyExercise(MainExercise):
    """
    The first exercise-type class
    It's prepare the logic and solution
    Math multiply
    Tuple with 4 numbers (int) needed.
    """

    def __init__(self, nums_tuple: tuple[int, int, int, int]):
        """Initialize the parameters."""
        self.x, self.y = self.get_random_parameters(nums_tuple)
        super().__init__()

    def get_ans(self) -> int:
        """Return the answer."""
        return self.x * self.y


class MediumExercise(MainExercise):
    """
    The second exercise-type class
    it's prepare the logic and solution
    multiply and sum
    tuple with 4 numbers (int) needed.
    """
    def __init__(self, nums_tuple: tuple[int, int, int, int]):
        self.x, self.y = self.get_random_parameters(nums_tuple)
        super().__init__()

    def get_ans(self) -> int:
        return self.x * self.y + self.x


class HardExercise(MainExercise):
    pass