"""The main construct file."""

from random import randint


class MainExercise:
    """The main exercise class."""

    def __init__(self):
        """Initialize the main exercise class."""
        pass

    def get_random_parameters(self):
        """Get a random parameters."""
        pass


class FirstTypeExercise(MainExercise):
    """
    The first type exercise class.
    It's prepare the parameters and solution.
    Tuple with 4 numbers (int) needed.
    """

    def __init__(self, nums_tuple: tuple):
        """Initialize the parameters."""
        self.x, self.y = self.get_random_parameters(nums_tuple)
        self.person_1, self.person_2 = self.get_persons_names()
        self.answer = self.get_ans()

    def get_random_parameters(self, num_set):
        """Get a random parameters."""
        a, b, c, d = num_set
        return randint(a, b), randint(c, d)

    def get_persons_names(self):
        """Get a random persons names."""
        name_1 = (
            'Коля', 'Вася', 'Петя', 'Борис',
            'Егор', 'Никита', 'Артур', 'Стас',
            'Максим', 'Дима', 'Витя', 'Данил'
            )

        name_2 = (
            'Сережа', 'Саша', 'Кузя',
            'Андрей', 'Паша', 'Семён',
            'Ярослав', 'Денис', 'Алексей',
            'Михаил', 'Артем'
            )

        return (
            name_1[randint(0, len(name_1) - 1)],
            name_2[randint(0, len(name_2) - 1)]
            )

    def get_ans(self):
        """Run the first type exercise."""
        return self.x * self.y
