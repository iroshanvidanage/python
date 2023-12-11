def moneyDipenser(available_notes, amount):
    outPutMoney = []

    for i in available_notes:
        outPutMoney.append(amount//i)
        amount %= i

    return outPutMoney


notesAvailable = [1000, 500, 100, 20, 10]
print(moneyDipenser(notesAvailable, 2650))

