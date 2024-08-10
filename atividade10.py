def primo(numb):
    if numb < 2:
        return False
    for e in range(2, int(numb ** 0.5) + 1):
        if numb % e == 0:
            return False
        return True

inicio = int(input("Digite o intervalo que você deseja: "))
fim = int(input("Agora digite o fim que deseja neste intervalo: "))

print(f"Números primos dos numeros {inicio} e {fim} são:")
for num in range(inicio, fim + 1):
    if primo(num):
        print(num)
