# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1=float(input("digite a nota 1"))
n2=float(input("digite a nota 2"))

if (n1+n2)/2 < 5:
    print(f"Sua nota foi de {(n1+n2)/2:.1f}, por conta disso você foi REPROVADO.")
elif (n1+n2)/2 > 5 and (n1+n2)/2 <6.9:
    print(f"Sua nota foi de {(n1+n2)/2:.1f}, como a média é 7 você ficou de RECUPERAÇÃO.")
else: 
    print(f"Sua nota foi de {(n1+n2)/2:.1f}, por conta disso você foi APROVADO.")