soma = 0

while True:
	numero = float(input(f"Digite seu número ou 0 para sair: "))
	if numero == 0:
		break
	soma += numero
	print(f"A soma dos números {numero:.0f} é: {soma:.0f}")
