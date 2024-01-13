"""Escribir un algoritmo que determine si un número N (entero), que ingresa un
usuario, es divisible por M."""


def ingresar_numero_entero():
    return int(input("Ingrese un numero: "))


def es_divisible(dividendo: int, divisor: int) -> bool:
    return dividendo % divisor == 0


def main():
    dividendo = ingresar_numero_entero()
    divisor = ingresar_numero_entero()
    if es_divisible(dividendo, divisor):
        print(f"El numero {dividendo} es divisible por {divisor}.")
    else:
        print(f"El numero {dividendo} NO es divisible por {divisor}.")


if __name__ == "__main__":
    main()
