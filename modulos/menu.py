from modulos.title import title
from modulos.clear import clear

def menu():
    print('##01 | <name_of_option>')
    print('##02 | <name_of_option>')
    print('##00 | Sair')
    try:
        choice_menu = int(input('| '))

        if choice_menu == 1:
            clear()
            title()
            print('01')
            input()
        elif choice_menu == 2:
            clear()
            title()
            print('02')
            input()
        elif choice_menu == 0:
            clear()
            title()
            input('- (Clique em qualquer lugar para encerrar)')
            
        else:
            clear()
            print('Insira um número dentro do alcance permitido!\n')
            menu()
    except ValueError as error:
        clear()
        print('Por favor insira apenas um dos números esperado.\n')
        menu()
