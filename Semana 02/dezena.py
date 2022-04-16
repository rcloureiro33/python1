numero = int(input("Entre com o número para achar a dezena: "))

unidade = numero % 10
dezena = numero % 100 

dez_restante = int((dezena - unidade) / 10)

print("A dezena do número",numero,"é : ",dez_restante)