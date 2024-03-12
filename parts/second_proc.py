"""SubFunctions and tools."""


def choose_plural(amount: int, word: tuple):
    """
    Three words in one tuple needed to choose plural.
    :param amount:
    :param word ['Врач', 'Врача', 'Врачей']:
    :return:
    """
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif (
        amount % 10 >= 2 and amount % 10 <= 4 and
        (amount % 100 < 10 or amount % 100 >= 20)
    ):
        variant = 1
    return '{} {}'.format(amount, word[variant])


def exercise_text(exemple, goods):
    """Prepare text to display."""
    plural = choose_plural

    result_text = (
        f'{exemple.person_1} купил {plural(exemple.x, goods)}\n'
        f'{exemple.person_2} купил в '
        f'{plural(exemple.y, ('раз', 'раза', 'раз'))} больше '
        f'{goods[-1]} \n'
        f'Саколько всего {exemple.person_2} купил {goods[-1]}?\n'
        )

    return result_text


def get_answer(exemple, goods):

    plural = choose_plural

    return (
        f'Всего {plural(exemple.answer, goods)}'
        )


def get_goods_list():
    """Get goods name."""
    word_1 = ('машина', 'машины', 'машин')
    word_2 = ('корабль', 'корабля', 'кораблей')
    word_3 = ('грузовик', 'грузовика', 'грузовиков')
    word_4 = ('самолет', 'самолета', 'самолетов')

    return [word_1, word_2, word_3, word_4]