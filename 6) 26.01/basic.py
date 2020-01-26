x = 12
y = 2.4

#print(x + y)
#print(x - y)
#print(x * y)
#print(x / y)
#print(x % y)
#print(x ** y)

s1 = 'ana are mere'
s2 = 'don\'t'

a = 'Ana'
m = 'mere'
s3 = '{} are {}'.format(a, m)
s4 = '{var_a} are {var_b}'.format(var_a=a, var_b=m)
#print(s3)

l = [1, 2, 3, 4, 5, 6, 7]

t = (1, 2, 3, 4, 5, 6, 7)

s = {1, 2, 3, 4, 5, 6, 7}

print('string', s1[0])
print('list', l[0])
print('tuplu', t[0])
print(l[-1]) #echivalent cu l[len(l)-1]
#print('set', s[0]) seturile nu au ordine

print(s1[4:7])
print(s1[4:])
print(l[:5])
print(l[:])
print(l[0:5:2])
print(l[::2])
print(l[5:0]) #nu da eroare
print(l[::-1])

print(len(s1))
print(len(l))
print(len(t))
print(len(s))

#string-urile sunt imutabile
s1_modif = s1.upper()
print(s1, s1_modif)
#listele sunt mutabile
l[0] = -1
print(l)
#tuplurile sunt imutabile
#t[0] = -1

#set=multime
set_nou = {1, 1, 1, 2, 2, 2, 2, 3, 3}
print(set_nou)

#metode
l.append(4)
l.extend([1, 2, 3])
print(l)

lista_randuri = [
    'primul',
    'al doilea',
    'al treilea', #se pune o "," in plus pentru commit-urile viitoare din git
]
print(lista_randuri)

d = {
    1: 'bau',
    2: 'miau',
    'cheia3': 123,
    'cheia4': 'string',
    (1, 'unu'): [1, 2, 3],
    #tuplurile pot fi chei in dictionar, listele si seturile nu
}
print(d)
print(d[(1, 'unu')])

d.pop(1)
#d[0] - referentierea directa da eroare
ceva = d.get(0, 'altceva')
print(ceva)
print(list(d.keys()))
print(list(d.values()))
print(d)
#del d[0] doar sterge, nu intoarce ce a sters

#pentru comparatii de numere si tipuri vezi demo Francisc

a = 2
b = 3
if a > b:
    print('da') # se printeaza doar daca e adevarata conditia
print('nu') # se printeaza mereu
if a > b:
    print('da')
elif a < b:
    print('nu')
else:
    print('poate')

if (
    a > b
    and x > y
):
    pass

for elem in [1, 2, 3]:
    print(elem)
    if elem == 2:
        break
else:
    print('gata')

# vezi demo Francisc pentru continuare
