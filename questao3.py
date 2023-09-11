duracao_seg = int(input(""))
minutos = duracao_seg // 60
segundos = duracao_seg % 60
horas = minutos // 60
m = minutos % 60
print(f'{horas}:{m}:{segundos}')
