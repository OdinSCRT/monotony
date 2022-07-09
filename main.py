# coding: utf-8
# code by Roberty and Guilherme

from lib import printd, banner, escolhas, inputf, inputi, printe, escolhas, pausa
from time import sleep

def nivel4():
	pass

def nivel3():
	banner()
	lista_de_compras = ["Leite", "Ovos", "Farinha", "Carne"]

	printd("Ok então, vamos reescrever a lista \ncom os itens na ordem correta")
	nova_lista_de_compras = inputi("Diga os itens separados por virgula").split(",")

	if lista_de_compras == nova_lista_de_compras:
		printd("\nPelo menos você lembra de comida")
		pausa()
		nivel4()

	else:
		printd("\nMemória fraca é seu forte")
		pausa()
		nivel3()

def nivel2():
	banner()
	printd("Como uma boa pessoa ansiosa você olha o celular na esperança \nde alguma mensagem, curiosamente tem de fato uma mensagem.\n\nEla diz : Ainda está disponível, me encontre ao lado do\nrestaurante La Puchi as 20.\n")

	sleep(2)

	printd("Com medo de ser um erro ou um provável sequestro você ignora, \npega o cartão de ônibus e vai trabalhar com uma lista de\ncompras para a geladeira:\n\n-Leite\n-Ovos\n-Farinha\n-Carne.\n")

	sleep(2)
	
	printd("Andando você se depara com mais uma vez o ônibus lotado,\nchegando no trabalho uma pilha de papéis para assinar e preencher.\nPapo vem assinatura vai, a hora passa e chega sua hora.")
	
	sleep(2)
	
	printd("\nComeça uma chuva, e seu horário de ir chega.\nEntrou na chuva é pra se molhar")
	
	sleep(2)
	
	printd("\nAinda precisa ir ao mercado, olha o bolso e percebe que a lista \nestá completamente molhada.")

	pausa()
	banner()
	printd("\n\nVocê se lembra dos itens da lista de compras?\n")

	escolhas("Sim", "Não")

	escolha = inputf("Eai, oque me diz")

	if escolha == "Sim" or escolha == "1":
		nivel3()

	elif escolha == "Não" or escolha == "2":
		banner()
		printd("Memória fraca é seu forte")
		pausa()
		nivel2()

	else:
		printe()
		nivel2()

def main():
	banner()

	printd("Embora fosse sexta-feira, ainda tem trabalho. ")
	printd("Com tudo e como todo bom trabalhador, você pode desligar\no despertador ou se praparar para mais um dia ...\n")

	escolhas("Levantar", "Dormir")

	escolha = inputf("Oque fazer")

	banner()

	if escolha == "Levantar" or escolha == "1":
		printd("Agora que o despertador esta desligado é hora de agir !")
		sleep(3)
		nivel2()

	elif escolha == "Dormir" or escolha == "2":
		printd("Voce nao foi trabalhar e foi demitido, parabéns vocé agora mora na rua . ")
		pausa()
		main()

	else:
		printe()
		main()

main()