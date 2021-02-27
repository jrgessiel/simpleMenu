# Gessiel

from modulos.title import title
from modulos.menu import menu
from modulos.clear import clear

title()
player_name = str(input('Me fale qual o seu nome, garoto(a). \n| '))
clear()

title()
print(f'Prazer em conhece-lo(a), {player_name}! Com base nas opções do menu abaixo, me diga o que quer fazer.')
menu()



