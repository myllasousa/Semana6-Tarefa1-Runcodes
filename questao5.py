preco = float(input(""))
preco_avista = preco - (preco * 9 / 100)
preco_5v = preco / 5
preco_10v = preco / 10
preco_10v2 = preco_10v + preco_10v * 17 / 100
print(f'{preco_avista:.2f}')
print(f'{preco_5v:.2f}')
print(f'{preco_10v2:.2f}')
