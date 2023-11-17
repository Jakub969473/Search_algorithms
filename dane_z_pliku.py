
def pobierz_dane():
    with open('dane_wejsciowe.txt') as file:
        x = iter(file)
        amount = int(next(x))
        start = int(next(x))
        end = int(next(x))

        if amount < 1:
            raise Exception("Amount must be greater than 0")
        elif start >= end:
            raise Exception("Start of range must be smaller than end")

        return [amount, start, end]

