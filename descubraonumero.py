#DESCUBRA O NÚMERO

from random import randint
segredo = randint(1, 10)
print("Seja Bem-vindo")
escolha = 0

while escolha != segredo:
	g = input("Digite um número entre 1 e 10: ")
	escolha = int(g)
	if escolha == segredo:
		print("Você acertou")
	else:
		if escolha > segredo:
			print("Muito alto")
		else:
			print("Muito Baixo")
print("Fim de Jogo")

