
def convert(score):
    if score == 0:
        return 0
    return score - 1 + 400

print('Entrada:' + str(0) + ' Saida:' + str(convert(0)))
print('Entrada:' + str(1) + ' Saida:' + str(convert(1)))
print('Entrada:' + str(50) + ' Saida:' + str(convert(50)))
print('Entrada:' + str(99) + ' Saida:' + str(convert(99)))
print('Entrada:' + str(100) + ' Saida:' + str(convert(100)))
