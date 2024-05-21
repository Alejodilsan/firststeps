operaciones = ['suma', 'resta', 'multi', 'divid']

print (' Bienvenidos a la caluladora')
print (' para salir escribe \'salir\'')
print ('Las operaciones son', operaciones)

resultado = ''

while True:
    if not resultado:
        resultado = input('ingrese numero   ')
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)
    op = input('Ingresa la operacion     ')
    if op.lower() == 'salir':
        break
    n2 = input('ingresa el siguiente numero:   ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

# Ahora se programa la logica de las sumas 

    if op.lower() == 'suma':
        resultado += n2
        #print (resultado)
    elif op.lower() == 'resta':
        resultado -= n2
        #print (resultado)
    elif op.lower() == 'multi':
        resultado *= n2
       # print (resultado) # en lugar de hacer varios print por cada operacion se hace el formateo de string print (f')
    elif op.lower() == 'divid':
        resultado /= n2 
        #print (resultado)
    else:
        print('operacion no valida')
        break
    
    print('el resultado es ',f'{resultado}')












# numero = 9 
# operacion = ['suma', 'multi', 'resta','divid']
# if numero == True:
#     print ('ingrese operacion  ')
#     if operacion 