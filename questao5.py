def preco_avista(preco):
    return preco - (preco * 9 / 100)

def preco_5v(preco):
    return preco / 5

def preco_10v(preco):
    return (preco + preco * 17 / 100) / 10

valor = float(input(""))
p1 = preco_avista(valor)
p2 = preco_5v(valor)
p3 = preco_10v(valor)
print(f'{p1:.2f}')
print(f'{p2:.2f}')
print(f'{p3:.2f}')
