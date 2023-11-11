

import pyttsx3

#inicialize o motor de sintaxe de fala

engine = pyttsx3.init()

#texto que você deseja que seja lido  em formato de audiobook

texto = input('Olá digite seu nome: ')

if texto == 'Hugo':
    texto ='Bem vindo Hugo, é um prazer ter você por aqui'
else:
    texto = 'Tente novamente com outro nome!'


#configuração da voz e da velocidade deleitura (opcional)
engine.setProperty('rate',130) #ajuste a velocidade conforme desejado


#gere o audiobook lendo o texto
engine.say(texto)

#aguarde até que a leitura seja concluida
engine.runAndWait()

#encerre o motor de sintese de fala
engine.stop()
