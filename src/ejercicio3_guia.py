"""Escribir un algoritmo que determine si un número entero, que ingresa un
usuario, es par."""


def es_par(numero: int) -> bool:
    return numero % 2 == 0


def main():
    numero = int(input("Ingrese un numero: "))
    if es_par(numero):
        print("El numero", numero, "es par.")
    else:
        print(f"El numero {numero} es impar.")


if __name__ == "__main__":
    main()
