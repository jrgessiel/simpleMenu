# Gessiel
# Estatísticas das partidas de Free Fire

#Nome do jogador

#Menu
    #Registrar partidas
        #Qual posição ficou
        #Quantos matou?
            #Quantos foram com tiro na cabeça?
        #Mais uma?
    #Ver último registro
    #Sair
    

#Partidas

#Vitorias

#Abates

#Detalhes
    #TOP 10
    #Taxa de abate
    #Taxa de tiro na cabeça
    #Porcentagem de vitorias

#Gravar em um arquivo externo que mantém sempre os ultimos valores
from modulos.title import title
from modulos.menu import menu
from modulos.clear import clear

title()
player_name = str(input('Me fale qual o seu nome, garoto(a). \n| '))
clear()

title()
print(f'Prazer em conhece-lo(a), {player_name}! Com base nas opções do menu abaixo, me diga o que quer fazer.')
menu()



