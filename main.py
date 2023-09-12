#Crie um programa que verifica se uma string é um palíndromo, ou seja, se ela é a mesma quando lida de trás para frente (desconsiderando espaços e maiúsculas/minúsculas).
def verifica_palindromo(texto):
  texto.replace(" ","").lower()
  if texto==texto[::-1]:
    print(f'{texto} é palindromo!')
  else:
    print(f'{texto} não é palindromo!')

texto=input('digite a palavra: ')
verifica_palindromo(texto)



