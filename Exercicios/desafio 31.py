distancia = float(input("""
==========================================================
A passagem custa R$0,50 por KM rodado até 200Km
excedido os 200Km passa a custar R$0,45 por Km rodado
==========================================================
Digite a distancia percorrida: """))
if distancia <= 200:
    print(f'Sua viagem tem {distancia}Km de distancia, você vai pagar no total: R${float(distancia * 0.50):.2f}')
else:
    print(f'sua viajem ultrapassou 200Km portanto pagara mais barato, valor a pagar: {float(distancia * 0.45):.2f} ')