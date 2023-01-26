import os
"""c = "abesato"
t = 0
i = 0
while i < len(c):
    if c[i] == 'a':
        t = t+1
    i = i+1
    print(t)
for i in range(1,10):
    print(i)
nome = 'paulo'
idade = 18
print('%s, você tem %d anos de idade'  %(nome, idade))
varr = 'abc'
print(f'{varr : >10} ')
print(f'{varr: <10} ')
var = 'Ola mundo'
print(var[0])
print(var[0:4])
print(var[4:])
print(var[:4])
print(len(var))
print(len(var[1]))
print(var[-1::-1])
numero1 = input("Digite um numero ")
try:
    numero = float(numero1)
    print("Isso é um numero ")
except:
    print("Isso não é um numero ")
var1 = 'id'
print(id(var1))
"""
os.system('cls' if os.name == 'nt' else 'clear')
lista = []
print(lista)
print(type(lista))
print(bool(lista))
lista = ['abc', 123, bool, 1.2, []]
print(type(lista[0]))
print(lista[0].upper())
lista[0] = 2
lista[1] = "abacate"
lista[2] = True
print(lista)
ab = '56789'
lista[1] = ab
nome = lista[0]
print(lista)
print(nome)
del lista[0]
print(lista[0])
lista.append("coe")
print(lista)
lista.pop()
print(lista)
aux = lista.pop()
print(aux)
lista.insert(0, 5)
print(lista)
lista.clear()
print(lista)
lista1 = ["joao", "jose" "joaquim" "junia"]
for i in lista1:
	print(i )

os.system('cls' if os.name == 'nt' else 'clear')

###Exibindo os indices de uma lista
nome = ["maria", "helena", "Luiz"]
for i in nome:
    print (i)
os.system('cls' if os.name == 'nt' else 'clear')
tupla = ("Abacate","José")
print(type(tupla))


os.system('cls' if os.name == 'nt' else 'clear')

var1 = 5/3
print(round(var1, 2))
