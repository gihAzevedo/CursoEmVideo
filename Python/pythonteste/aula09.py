'''
frase = 'Curso em Video Python'
print(frase) #Mostra completo#
print(frase[3]) #Mostra apenas a letra S, que é a terceira string começa no 0 #
print(frase[3:13]) #Vai da letra S(3) até e(13)#
print(frase[:13]) #Vai do inicio até e(13)#
print(frase[1:15:2]) # Vai começar na letra U(1) e vai até a string 15, entretanto pulando de 2 em 2
'''
'''
#Print de mais de uma linha#
print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fourtunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for begginers to use and learn, so jump in!""")
'''
frase = 'Curso em Video Python'
print(frase.count('o')) #Conta quantas letras possui na frase#
print(frase.upper().count('O')) #Transforma todas as letras em maiscula e conta quantas letras O #
print(len(frase))#Conta quantos caracteres possui a frase#
print(len(frase.strip())) #Tira os espaços no final e no começo#
print(frase.replace('Python', 'Android'))#Substitui a cadeia de caractere pelo outro#
print('Curso' in frase) #Verifica se a palavra esta dentro da frase#
print(frase.find('Curso')) #Vai mostrar a posição onde começa a palavra #
print(frase.lower().find('video')) #Vai transformar em minusculo e mostrar a posição inicial#
print(frase.split()) #Divide a frase#
dividido = frase.split()
print(dividido[0]) #Vai mostrar apenas o primeiro conjunto#
print(dividido[2][3]) #Vai mostrar o terceiro caractere do segundo conjunto, inicia no 0#

