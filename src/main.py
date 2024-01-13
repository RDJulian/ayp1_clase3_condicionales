def evaluar_edad(edad: int) -> None:
    if edad < 0:
        print("No es posible esa edad")
    elif edad >= 18:
        print("Es mayor de edad")
        if edad >= 65:
            print("Te podes jubilar")
    else:
        print("Es menor de edad")


def main():
    edad = int(input("Ingrese su edad: "))
    evaluar_edad(edad)


if __name__ == "__main__":
    main()
