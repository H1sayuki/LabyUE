def lista_liczb1(liczby):
    for i in range(len(liczby)):
        liczby[i] *= 2
    return liczby


print(lista_liczb1([2, 4, 6, 8, 10]))


def lista_liczb2(liczby):
    pomnozone = [x * 2 for x in liczby]
    return pomnozone


print(lista_liczb2([2, 4, 6, 8, 10]))
