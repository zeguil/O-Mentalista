import random
import time
import os

# mostrar titulo
def titulo():
    print('\n############################')
    print('\t O MENTALISTA')
    print('############################')

# gerandor de numero aleatorio
def gerador_numerico():
    numero_gerado = random.randrange(1, 101)
    return numero_gerado

# função principal
def mentalista(numero, tentativa):
    while True:
        try:
            chute = int(input('\nChute o numero que estou pensando entre 1 e 100.\nResposta: '))
            if chute > 100 or chute < 1:
                time.sleep(1)
                print('\nApenas um numero entre 1 e 100, tente de novo')
            elif chute > numero:
                time.sleep(1)
                print(f'\nO numero que pensei é menor que {chute}, tente de novo.')
                tentativa += 1
                time.sleep(1)
            elif chute < numero:
                time.sleep(1)
                print(f'\nO numero que pensei é maior que {chute}, tente de novo.')
                tentativa += 1
                time.sleep(1)
            elif chute == numero:
                time.sleep(1)
                print(f'\nPARABÉNS, você acertou com {tentativa} tentativas!\n')
                time.sleep(1)
                opcao=input('Quer jogar mais uma vez? (s/n): ')
                if opcao.lower() == 's':
                    print('\nReiniciando jogo...')
                    time.sleep(3)
                    numero = gerador_numerico()
                    tentativa = 0
                    os.system('cls')
                    titulo()
                    continue
                elif opcao.lower() == 'n' or 'nao':
                    time.sleep(1)
                    print('\nOk, obrigado por jogar!')
                    break
        except ValueError:
            print("\nDigite um numero inteiro!")
            time.sleep(1)


titulo()
input('Digite ENTER para iniciar o game...')
numero  = gerador_numerico()
tentativas = 0
mentalista(numero, tentativas)

    

