# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas
print('preço de viagem')
km = float(input("Digite KM de sua viagem:"))
if km<200:
    print(f"você tem que pagar:R${km*0.5}")
else:
    print(f'você tem que pagar:R${km*0.45}')