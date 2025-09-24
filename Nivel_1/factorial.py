def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(512))
