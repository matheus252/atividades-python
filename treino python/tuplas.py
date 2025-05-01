#são imutaveis

halogenios = ('f','cl','i','at')
gases_nobre = ('he','ne','ar','xe')
elementos = halogenios + gases_nobre
t1 = (5,3,4,2,5,6,6,88,9,75,4,3,2,)
print(max(t1))

#operações não disponiveis em tuplas :sort(), .append(), reverse(), pop()

# for elemento in elementos:
#     print(f'elemento quimico: {elemento}')

# grupo17 = list(halogenios)
# grupo17[0] = 'h'
# print(grupo17)

gbrupo1 = ['li','na','k','rb', 'cs']
alcalinos =  tuple(gbrupo1)
print(type(alcalinos))

print(sorted(alcalinos))
