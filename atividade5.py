def get_in():
    while true:
        try:
            num = int(input("Digite um número de 1 a 10:"))
            break
        except:
            print("Você está digitando o número impar considerado errado, tente novamente.")
            Print(num)
