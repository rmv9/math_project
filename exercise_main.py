"""Titul process file."""

from parts import first_proc as first
from parts import second_proc as second
from random import choice


if __name__ == "__main__":

    NUMS_SET = (3, 9, 4, 9)

    exe_auto = first.FirstTypeExercise(NUMS_SET)
    shuff = choice(second.get_goods_list())

    print(second.exercise_text(exe_auto, shuff), end='\n\n')

    while True:
        print(f'Сколько {shuff[-1]} купил {exe_auto.person_2}')
        if (int(input())) == exe_auto.answer:
            print('\nВерно!')
            print(second.get_answer(exe_auto, shuff), end='\n\n')
            break
        print('\nНеверно!')
