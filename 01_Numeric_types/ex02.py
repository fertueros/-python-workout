#!/usr/bin/env python3


def suma(*args):
    total = 0

    for arg in args:
        total += arg

    return total


# Ejemplo de uso
print(suma(1, 2, 3, 5))  # Salida: 11
