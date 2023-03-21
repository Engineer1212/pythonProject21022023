numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def evenNumber(number):
    if number % 2 == 0:
        return True
    else:
        return False


# filter(fn, parametre_listesi)
#evenNumbers = list(filter(evenNumber, numbers))
#print(evenNumbers)


evenNumbers =list(filter(lambda x: x % 2 == 0, numbers))
print(evenNumbers)