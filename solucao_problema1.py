qntTestes = int(input('Informe a quantidade de testes:'))
# adiciona ao Array os testes a se fazer
a = 0
qntPalitos = []
while a < qntTestes:
    valorTestado = int(input('Informe quantos palitos (2 até 100):'))
    qntPalitos.append(valorTestado)
    a += 1
    pass
#Validar os maiores valores
maxValor = 0
maxValores =[]
posPal=0
while posPal < qntTestes:
    if qntPalitos[posPal]%2 == 1:
        maxValor = '7'
        qntUm = qntPalitos[posPal]//2
        while qntUm > 1:
            maxValor += '1'
            qntUm -= 1
#Como o python não permite alterar um caracter específico, vai ser necessário converter o string pra um array e trabalhar nele.
    else:
        maxValor = '1'
        qntUm = qntPalitos[posPal]/2
        while qntUm > 1:
            maxValor = maxValor + '1'
            qntUm -= 1
        pass
    maxValores.append(int(maxValor))
    posPal+= 1
pass

#Validar os menores valores
valoresBase = [108,188,200,208,288,688,888]
posPal = 0
minValor = 0
minValores = []
cont = 0
acaba = False
while posPal < qntTestes:
    #aqui é um bloco que o sistema vai analisar todas as possibilidades que não tem uma lógica
    if qntPalitos[posPal] < 15:
        valPalit = [1, 7, 4, 3, 0, 8, 10, 18, 22, 20, 28, 68, 88]
        pos = qntPalitos[posPal] - 2
        minValor = valPalit[pos]
        acaba = True
    pass
    # aqui o sistema vai definir qual a posição do array pra usar pra fazer as contas
    base = qntPalitos[posPal]
    if base > 14:
        while base > 14:
                base = base - 7
                cont += 1
        pass
        posArray = base - 15
    pass
    #aqui o sistema vai definir o valor mínimo que pode ser usado
    if acaba == False:
        minValor = valoresBase[posArray]
        while cont > 0:
            minValor = minValor * 10 + 8
            cont -= 1
            pass
    pass
    minValores.append(minValor)
    cont = 0
    minValor = 0
    acaba = False
    posPal += 1
pass
imp = 0
while imp < qntTestes:
    print(f'para {qntPalitos[imp]} palitos, os valores são: {minValores[imp]} e {maxValores[imp]}')
    imp += 1
    pass