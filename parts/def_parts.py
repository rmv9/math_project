"""Functions and tools."""

from parts import class_parts as cl

from parts import def_parts as func

from random import choice


def choose_plural(amount: int, goods: tuple[str, str, str]) -> str:
    """Takes and return correct plural.

    Args:
        amount (int): Amount of goods.
        goods (tuple): Tuple with words.

    Seealso:
        sample of tuple : ('Врач', 'врача', 'врачей')

    Returns:
        str: number of amount and one word in correct plural.
    """
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif (
        amount % 10 >= 2 and amount % 10 <= 4 and
        (amount % 100 < 10 or amount % 100 >= 20)
    ):
        variant = 1
    return '{} {}'.format(amount, goods[variant])


def exercise_text(exercise, goods: tuple[str, str, str]) -> str:
    """Prepare text to display.

    Args:
        exercise (FirstTypeExercise) : Object, exemplar.
        goods (tuple) : Tuple with words.

    Returns:
        str : Text of exercise.

    Seealso:
        sample of tuple : ('Врач', 'врача', 'врачей')
        sample of exercise : FirstTypeExercise(3, 9, 5, 9)
        sample of result_text :
            Коля купил ... машин
            Вася купил в ... раз больше машины
            Сколько всего машин купил Вася?
    """
    plural = choose_plural

    result_text = (
        f'{exercise.person_1} купил {plural(exercise.x, goods)}\n'
        f'{exercise.person_2} купил в '
        f'{plural(exercise.y, ('раз', 'раза', 'раз'))} больше '
        f'{goods[-1]} \n'
        f'Сколько всего {goods[-1]} купил {exercise.person_2}?\n'
        )

    return result_text


def get_answer(exercise, goods: tuple[str, str, str]):
    """Get answer to the last exercise.

    Args:
        exercise (FirstTypeExercise) : Object, exemplar.
        goods (tuple) : Tuple with words.

    Seealso:
        sample of exercise : FirstTypeExercise(3, 9, 5, 9)
    """
    plural = choose_plural

    return (
        f'Всего {plural(exercise.answer, goods)}'
        )


def get_goods():
    """Get goods name."""
    words_array = [
        ('машина', 'машины', 'машин'),
        ('корабль', 'корабля', 'кораблей'),
        ('грузовик', 'грузовика', 'грузовиков'),
        ('самолет', 'самолета', 'самолетов')
    ]

    return words_array


def do_exercise() -> int:
    """Start and finish one exercise."""
    NUMS_SET: tuple[int, int, int, int] = (3, 9, 4, 9)

    exe = cl.FirstTypeExercise(NUMS_SET)
    shuff = choice(func.get_goods())

    print(func.exercise_text(exe, shuff), end="\n\n")

    while True:
        print(
            f'Сколько {shuff[-1]} купил {exe.person_2}\n'
            f'TEST: {exe.answer}'
            )
        if (int(input())) == exe.answer:
            print("\nВерно!")
            print(func.get_answer(exe, shuff), end="\n\n")
            return 1
        print("\nНеверно!\n")


def main() -> None:
    """Main logic."""
    WORDS = ('задача', 'задачи', 'задач')
    exe_amount: int = int(input('Сколько задач хотите решить?\n'))
    level: int = int(input('Уровень сложности?\n1-легко\n2-средне\n'))

    match level:
        case 1:
            result = [func.do_exercise() for _ in range(exe_amount)]
        case 2:
            pass
        case _:
            pass 

    print(f'Решено: {choose_plural(sum(result), (WORDS))}')
