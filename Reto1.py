#recibir un numero por teclado y determinar si este es multiplo de 5
numero=int(input('Digite un numero Entero:\n'))

resultado=numero%3

print(f'el residuo es: {resultado}')

#condicional simple en python

if(resultado==0):
    print(f'el numero {numero} es multiplo de 3 ')
else:print('el Numero no es multiplo de 3')
print('fin del programa')