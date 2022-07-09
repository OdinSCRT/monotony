# coding: utf-8
# code by Roberty and Guilherme

import os
from random import choice
from time import sleep

'''
Relação de Codigo de Cores

VERMELHO = 1
AMARELO  = 2
AZUL     = 3
CIANO    = 4
VERDE    = 5
ZERADO   = 6
NEGRITO  = 7

'''

colorsn = ["",
		  "\033[1;31m",
		  "\033[1;93m",
		  "\033[1;34m",
		  "\033[1;36m",
		  "\033[0;32m",
		  "\033[0;0m",
		  "\033[;1m"]

def printd(dialog):
	# Usado para dialogo
	print(f"{colorsn[3]}{dialog}{colorsn[6]}")

def banner():
    # Banner do game
    colors = ["\033[1;31m",
          	  "\033[1;93m",
          	  "\033[1;34m",
          	  "\033[1;36m",
          	  "\033[0;32m",]

    by_roberty = "Code By: Roberty"
    by_guilherme = "History By: Guilherme"

    os.system("clear")
    print("\n")
    print(f"{choice(colors)} __  __ {choice(colors)}     {choice(colors)}       {choice(colors)}     {choice(colors)} _  {choice(colors)}     {choice(colors)}       {choice(colors)}      {colorsn[6]}")
    print(f"{choice(colors)}|  \/  |{choice(colors)}     {choice(colors)}       {choice(colors)}     {choice(colors)}| | {choice(colors)}     {choice(colors)}       {choice(colors)}      {colorsn[6]}")
    print(f"{choice(colors)}| \  / |{choice(colors)} ___ {choice(colors)} _ __  {choice(colors)} ___ {choice(colors)}| |_{choice(colors)} ___ {choice(colors)} _ __  {choice(colors)}_   _ {colorsn[6]}")
    print(f"{choice(colors)}| |\/| |{choice(colors)}/ _ \{choice(colors)}| '_ \ {choice(colors)}/ _ \{choice(colors)}| __{choice(colors)}/ _ \{choice(colors)}| '_ \|{choice(colors)} | | |{colorsn[6]}")
    print(f"{choice(colors)}| |  | |{choice(colors)} (_) {choice(colors)}| | | |{choice(colors)} (_) {choice(colors)}| ||{choice(colors)} (_) {choice(colors)}| | | |{choice(colors)} |_| |{colorsn[6]}")
    print(f"{choice(colors)}|_|  |_|{choice(colors)}\___/{choice(colors)}|_| |_|{choice(colors)}\___/{choice(colors)} \__{choice(colors)}\___/{choice(colors)}|_| |_|{choice(colors)}\__, |{colorsn[6]}")
    print(f"{choice(colors)}        {choice(colors)}     {choice(colors)}       {choice(colors)}     {choice(colors)}    {choice(colors)}     {choice(colors)}       {choice(colors)} __/ |{colorsn[6]}")
    print(f"{choice(colors)}        {choice(colors)}     {choice(colors)}       {choice(colors)}     {choice(colors)}    {choice(colors)}     {choice(colors)}       {choice(colors)}|___/ {colorsn[6]}")
    color_x = choice(colors)
    print(16*f"{color_x}-" + colorsn[2]+by_roberty+colorsn[6] + 16*f"{color_x}-")
    print(" " + 12*f"{color_x}-" + colorsn[2]+by_guilherme+colorsn[6] + 13*f"{color_x}-"+f"\n{colorsn[6]}")

def escolhas(*opcoes):
    # Cria a caixa de opções
    maior_string = max(len(i) for i in opcoes)
    strings_corrigidas = list()

    if maior_string >= len("Opções"):
        falta = maior_string - len("Opções")
        print((maior_string + 2) * f"{colorsn[5]}-{colorsn[6]}")
        print((f"{colorsn[5]}|{colorsn[6]}"+f"{colorsn[3]}Opções{colorsn[6]}")+falta * " " + f"{colorsn[5]}|{colorsn[6]}")

    elif maior_string < len("Opções"):
        maior_string = len("Opções")
        print((maior_string + 2)* f"{colorsn[5]}-{colorsn[6]}")
        print(f"{colorsn[5]}|{colorsn[6]}"+f"{colorsn[3]}Opções{colorsn[6]}"+f"{colorsn[5]}|{colorsn[6]}")

    print((maior_string + 2)* f"{colorsn[5]}-{colorsn[6]}")

    for i in opcoes:
        if len(i) <= maior_string:
            falta = maior_string - len(i)
            print((f"{colorsn[5]}|{colorsn[6]}"+f"{colorsn[2]}{i}")+ falta * f" {colorsn[6]}" + f"{colorsn[5]}|{colorsn[6]}")

    print((maior_string + 2)* f"{colorsn[5]}-{colorsn[6]}")        

def inputf(string):
    # Entrada de dados customizada
    return str(input(f"\n{colorsn[3]}{string}{colorsn[5]}?{colorsn[6]} "))

def inputi(string):
    # Entrada de dados customizada
    return str(input(f"\n{colorsn[3]}{string}{colorsn[5]}:{colorsn[6]} "))

def printe(erro=""):
    # Saida de erros
    strings = ["Não foi o que perguntamos",
               "Não está coerente as perguntas",
               "Não entendi o que quis dizer",
               "Escreva direito na próxima",
             '''01010110 01101111 01100011 11101010\n00100000 01110000 01110010 01101111\n01100011 01110101 01110010 01101111\n01110101 00100000 01110000 01101111\n01110010 00100000 01101001 01110011\n01110011 01101111 00100000 00111111''']

    msg = str()

    if erro == "":
        msg = choice(strings)

    banner()
    print(f"{colorsn[1]}Error!, {msg}{colorsn[6]}")
    sleep(3)

def pausa():
    input(f"\n{colorsn[5]}Pressione enter para continuar...{colorsn[6]}")