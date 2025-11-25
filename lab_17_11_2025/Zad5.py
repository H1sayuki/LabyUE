def contains_value(lst: list[int], value: int) -> bool:
    return value in lst


print(contains_value([1, 2, 3], 2))  # True
print(contains_value([1, 2, 3], 5))  # False
