import time
import emoji
print(f'{"FALTAM 10 SEGUNDOS PARA O ANO NOVO":=^40}')
for fogos in range(10,0,-1):
    time.sleep(1)
    print(fogos)
print(emoji.emojize(f':fireworks:FOGOS ESTOURANDO:fireworks:'))
