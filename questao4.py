=def media(nota1, nota2, nota3, nota4, nota5):
     return (nota1 + nota2 + nota3 + nota4 + nota5) / 5

n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))
n4 = int(input(""))
n5 = int(input(""))
m = media(n1, n2, n3, n4, n5)
print(max(n1, n2, n3, n4, n5))
print(min(n1, n2, n3, n4, n5))
print(m)
