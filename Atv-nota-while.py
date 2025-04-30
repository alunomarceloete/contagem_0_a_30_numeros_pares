# ATIVIDADE 02: ESTRUTURA DE DECISÃO E REPETIÇÃO. Aluno: Marcelo Santos

nota1 = float(input('Digite a 1ª Nota: '))
while nota1 < 0 or nota1 > 10:
    print('O número digitado é inválido, digite uma nota de 0 à 10')
    nota1 = float(input('Digite a 1ª Nota: '))      

nota2 = float(input('Digite a 2ª Nota: '))
while nota2 < 0 or nota2 > 10:
    print('O número digitado é inválido, digite uma nota de 0 à 10')
    nota2 = float(input('Digite a 2ª Nota: '))  

final = nota1 + nota2 / 2

if final >= 6:
    print('Sua média é:', final, 'Parabéns, você foi aprovado.')
else:
    print('Sua média é: ', final,'Você não atinigu a média suficiente para aprovação')