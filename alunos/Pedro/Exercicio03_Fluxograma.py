var_1 = int(input("Digite a 1º nota: "))
var_2 = int(input("Digite a 2º nota: "))
var_3 = int(input("Digite a 3º nota: "))

if var_1 > var_2:
    if var_1 > var_3:
        maior = var_1
    else:
        maior = var_3
else:
    if var_2 > var_3:
        maior = var_2
    else:
        maior = var_3

print(f"A maior variável é {maior}")