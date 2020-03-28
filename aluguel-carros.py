'''Aluguel de Carros.
R$60 por dia e R$0,15 por km rodado.'''

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Qual a quantidade de km rodados? km'))

pago = (dias * 60) + (km * 0.15)

print(f"Valor total a pagar: R${pago:.2f}")