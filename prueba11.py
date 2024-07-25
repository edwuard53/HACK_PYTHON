def cuadrado(numero):
 return numero * numero
lista = "abcdef"
lista = lista.split()
#lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)
print (resultado)
lista_resultado = list(resultado)
print(lista_resultado)
