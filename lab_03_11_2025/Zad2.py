def listaliczb1(liczby):
    for i in range(len(liczby)):
        liczby[i]*=2
    return liczby

print(listaliczb1([2,4,6,8,10]))

def listaliczb2(liczby):
    pomnozone=[x*2 for x in liczby]
    return pomnozone
print(listaliczb2([2,4,6,8,10]))