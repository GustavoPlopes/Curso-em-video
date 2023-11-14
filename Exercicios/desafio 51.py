num = int(input('Digite o primeiro termo da PA: '))
num2 = int(input('Digite a razão da PA: '))

for pa in range(0, 10):
    num += num2
    print(num, end=' → ')
print('FIM')
