# Ejercicio 1
usuarios = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for usuario in usuarios:
  if usuario == 'cersei':
    print(f'Lo siento, {usuario}, no tienes acceso')
    continue 
  else:
    print(f'{usuario} tienes acceso')

# Ejercicio 2
    def suma (a,b,c):
      return a+b+c
    resultado = suma(2,4,6)
    print(resultado)

# Ejercicio 3
    suma_lambda= lambda a,b,c: a+b+c
    resultado = suma_lambda(2,4,6)
    print(resultado)

# Ejercicio 4
nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for usuario in lista_nombre:
    if usuario == nombre:
        print(f"{nombre} está en la lista.")
        break
else:
    print(f"{nombre} NO está en la lista.")
    

