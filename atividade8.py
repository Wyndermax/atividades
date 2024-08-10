def par_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

num = int(input("Digite um número: "))
result = par_impar(num)
print(f"O número {num} é {result}.")

