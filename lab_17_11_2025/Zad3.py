def is_even(number: int) -> bool:
    return number % 2 == 0


value = is_even(7)

if value:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
