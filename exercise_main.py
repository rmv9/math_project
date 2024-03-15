"""Titul process file."""

from parts import class_parts as cl
from parts import def_parts as func
from random import choice


if __name__ == "__main__":

    NUMS_SET = (3, 9, 4, 9)

    exe_auto = cl.FirstTypeExercise(NUMS_SET)
    shuff = choice(func.get_goods())

    print(func.exercise_text(exe_auto, shuff), end="\n\n")

    while True:
        print(f"Сколько {shuff[-1]} купил {exe_auto.person_2}")
        if (int(input())) == exe_auto.answer:
            print("\nВерно!")
            print(func.get_answer(exe_auto, shuff), end="\n\n")
            break
        print("\nНеверно!")
