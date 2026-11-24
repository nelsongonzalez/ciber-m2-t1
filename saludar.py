import random


def saludo1() -> str:
    return "Hola"


def saludo2() -> str:
    return "Buenos días"


def saludo3() -> str:
    return "Hola, ¿Qué tal?"


def main() -> None:
    saludo = random.randint(0, 2)  # nosec B311

    if saludo == 0:
        print(saludo1())
    elif saludo == 1:
        print(saludo2())
    elif saludo == 2:
        print(saludo3())
    else:
        print("Adios")


if __name__ == "__main__":
    main()
