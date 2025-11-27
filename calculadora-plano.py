print("Calculador de Plano de Saúde")

print("\nSeja Bem-Vindo Misael Gonçalves de Lima")
#Definição das Variaveis Valor Base e idade
vb = float(input("\nDigite o valor Base do Plano R$: "))
idade = int(input("Insira a Idade do Cliente "))
# Adição da varivel valor mensal
valor_mensal = 0
# Calculo do mensal
if idade >= 0 and idade < 19:
    valor_mensal = vb * 100/100
elif idade >= 19 and idade < 29:
    valor_mensal = vb * 150/100
elif idade >= 29 and idade < 39:
    valor_mensal = vb * 225/100
elif idade >= 39 and idade < 49:
    valor_mensal = vb * 240/100
elif idade >= 49 and idade < 59:
    valor_mensal = vb * 350/100
elif idade >= 59:
    valor_mensal = vb * 600/100
else:
    print("Idade inválida. Por favor, insira um valor maior ou igual a zero.")
# Exibindo o valor final
print(f"\nLevando em consideração um cliente com {idade} anos, o valor mensal do plano é de: R$ {valor_mensal:.2f}") #