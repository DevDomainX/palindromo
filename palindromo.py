#!/usr/bin/env python3 
from colorama import init, Fore, Style
from time import sleep as x
import os as t
import sys
init()

def anagrama():
    while True:
        t.system("clear")
        title = Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"""
                > Create by: Hans Saldias <

                > by: 1LugarParaProgramar <

        Script para ver si una palabras o frases es \'palindromo\'
\n"""
        for i in title:
            print(i, end="", flush=True)
            x(0.1)
        frase = input("Ingrese frase o palabra: ")
        reves = frase[::-1]
        if frase == reves:
            print("Analizando.....\n")
            x(5)
            print(f"** La frase < {frase} > es \'palindromo\' **")
            op = input("Desea ingresar otra frase? si = (s) o no = (n): ").lower()
            if op == 's':
                anagrama()
            else:
                sys.exit()
        else:
            print(f"\nLo siento < {frase} > no es \'palindromo\'")
            op = input("Desea ingresar otra frase? si = (s) o no = (n): ").lower()
            if op == 's':
                anagrama()
            else:
                sys.exit()




if __name__ == '__main__':
    anagrama()