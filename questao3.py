def duracao(minutos, segundos, horas):
    return minutos, segundos, horas

duracao_seg = int(input(""))
minutos = duracao_seg // 60
segundos = duracao_seg % 60
horas = minutos // 60
m = minutos % 60
duracao(minutos, segundos, horas)

print(f'{horas}:{m}:{segundos}')
