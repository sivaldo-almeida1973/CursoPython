"""
Criação de personagem do mundo ficticio, apresentando apresentando
opções de acordo com os tipos de variáveis.

"""
print('-----------Bem Vindo --------------')
print('-----------Crie seu personagem --------------')

corCabelo = input('Digite a cor do cabelo: ')
corPele = input('Digite a cor da pele: ')
classe = input('Digite a sua classe dentre:\n 1-Guerreiro\n2-Mago\n3-Arqueiro\n4-Opção: ')
idade = int(input('Digite sua idade em anos: '))
altura = float(input('Digite a sua altura em metros: '))
habilidade_especifica = input('Digite a sua abilidade: ')
print('---------------Personagem Criado---------------------')

print(f'Seu personagem tem:\n'
      f'Cabelo: {corCabelo}\n'
      f'Pele: {corPele}\n'
      f'Classe:{classe}\n'
      f'Idade:{idade}\n'
      f'Altura {altura}\n'   
      f'abilidade é: {habilidade_especifica}')
