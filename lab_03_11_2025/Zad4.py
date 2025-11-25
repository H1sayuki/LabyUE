def co_drugi(liczby):
    for i in range(len(liczby)):
        if i % 2 == 1:
            print(liczby[i])


co_drugi([1, 11, 3, 42, 5, 16, 7, 88, 9, 14])
