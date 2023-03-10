Rodas = 10
Pessoas = 8
peso = 6000

print("Quantas rodas tem o seu veículo?")
Rodas = int(input())
print("Qual o peso do seu veículo ?")
Peso = int(input())
print("Seu veículo acomada quantas pessoas?")
Pessoas = int(input())
if Rodas == 3:
    print("Categoria A")
elif (Rodas == 4 and Pessoas == 8 and Peso == 3500):
    print("Categoria B")
elif (Rodas == 4 and Peso >= 3500):
    print("Categoria C")
elif (Rodas >= 4 and Pessoas > 8):
    print("Categoria D")
elif (Rodas >= 4 and Peso > 6000):
    print("Categoria E")