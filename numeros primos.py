'''Escribir un programa que pida al usuario un número entero y muestre por pantalla 
si es un número primo o no.'''

while True:
    num = int(input('\nIngrese numero: '))

    if num==2 or num==3 or num==5 or num==7:  
        print('Es numero primo')
    
    elif num%2==0 or num%3==0 or num%5==0 or num%7==0 or num%9==0:  
        print('No es numero primo')

    else:
        print('Es numero primo') 


