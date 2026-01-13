def merge_and_cube(list1: list[int], list2: list[int]) -> list[int]:
    merged = list(set(list1 + list2))
    return [x ** 3 for x in merged]


print(merge_and_cube([1, 2, 3], [2, 3, 4]))  # [64, 1, 8, 27]
