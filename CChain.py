# -*- coding: utf-8 -*-
# Python 3
#
#                 ██████╗ ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗
#                ██╔════╝██╔════╝██║  ██║██╔══██╗██║████╗  ██║
#                ██║     ██║     ███████║███████║██║██╔██╗ ██║
#                ██║     ██║     ██╔══██║██╔══██║██║██║╚██╗██║
#                ╚██████╗╚██████╗██║  ██║██║  ██║██║██║ ╚████║
#                 ╚═════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
#                                                         By: LawlietJH
#                                                              v1.1.4

import os
import sys

Autor = "LawlietJH"
Version = "v1.1.4"



#=============================================================================
#================================ Hexadecimal ================================
#=============================================================================



def Hex_Asc(Hex):	#~ Hexadecimal a Ascii
	
	Hex = Hex.replace(" ", "")		#~ Quita los espacios.

	Ascii = ''.join((chr(int(Hex[i:i+2], 16)) for i in range(0, len(Hex), 2)))
	
	return Ascii



def Hex_Bin(Hex):	#~ Hexadecimal a Binario.
	
	cont = 0
	Binario = ""
	Hex = Hex.replace(" ", "")		#~ Quita los espacios.

	Bin = ''.join((bin(int(Hex[i:i+2], 16))[2:].zfill(8) for i in range(0, len(Hex), 2)))
	
	#~ Se Separa la Cadena con un Espacio en Cada Byte.
	for b in Bin:
		
		cont += 1
		
		if(cont <= 7):
			Binario = Binario + b
		
		else:
			Binario = Binario + b + " "
			cont = 0
	
	return Binario



def Hex_Dec(Hex):	#~ Hexadecimal a Decimal.
	
	xD = ""
	Cont = 0
	Lista = []
	Decimal = ""
	
	Hex = Hex.upper()				#~ Pone Todo En Mayusculas.
	Hex = Hex.replace(" ", "")		#~ Quita Los Espacios.
	
	
	#~ Se Separa la Cadena con un Espacio en Cada Número.
	for i in Hex:
		
		Cont += 1
		
		if Cont % 2 != 0:
			xD = xD + i
			
		else:
			xD = xD + i
			Lista.append(str(eval("0x" + xD)) + " ")	#~ Se Añade Cada Número a la Lista.
			xD = ""
	
	for Dec in Lista:	#~ Se Añade Cada Número a la Cadena. 
		Decimal += Dec
	
	return Decimal



#=============================================================================
#=================================== Ascii ===================================
#=============================================================================



def Asc_Hex(Ascii):	#~ Ascii a Hexadecimal.
	
	cont = 0
	Hexadecimal = ""
	
	Hex = ''.join((hex(ord(c))[2:] for c in Ascii))
	
	#~ Se Separa la Cadena con un Espacio en Cada Byte.
	for x in Hex:
		
		cont += 1
		
		if cont % 2 != 0:
			Hexadecimal += x
					
		else:
			Hexadecimal += x + " "
			
	return Hexadecimal



def Asc_Bin(Ascii):	#~ Ascii a Binario.
	
	cont = 0
	Binario = ""

	Bin = ''.join((bin(ord(c))[2:].zfill(8) for c in Ascii))
	
	#~ Se Separa la Cadena con un Espacio en Cada Byte.
	for b in Bin:
		
		cont += 1
		
		if(cont <= 7):
			Binario = Binario + b
		
		else:
			Binario = Binario + b + " "
			cont = 0
	
	return Binario



def Asc_Dec(Ascii):	#~ Ascii a Decimal.
	
	Lista = []
	Decimal = ""
	
	for Letra in Ascii:				#~ Se Añaden los Caracteres a la Lista
		Lista.append(ord(Letra))	#~ Convertidos en su Respectivo Decimal.  
	
	for Dec in Lista:				#~ Se Añaden los Números a la Cadena.
		Decimal += str(Dec) + " "
	
	return Decimal



#=============================================================================
#================================== Decimal ==================================
#=============================================================================

def Dec_Bin(Dec):
	#~ Decimal a Hexadecimal.
	
	lista = []
	lista2 = []
	xD = ""
	Binario = ""

	#~ Se toma cada caracter hasta que encuentre un espacio
	#~ y esta cadena se agrega a una lista para convertir posteriormente.
	for num in Dec:
		
		if num != " ":
			xD = xD + num
		
		else:
			xD = bin(int(xD))
			lista.append(xD[2:])
			xD = ""
			
	xD = bin(int(xD))
	lista.append(xD[2:])
	
	#~ Se Añaden los 0 Faltantes al Inicio.
	for binario in lista:
		xD = binario
		while True:
			if len(xD) % 8 != 0:
				xD = "0" + xD
			else: 
				lista2.append(xD)
				break
	
	print("\n\n [+] Binario: \n\n >> ", end='')
	
	for Dec in lista2:
		print(Dec, end=' ')
	
	print("")



#=============================================================================
#================================== Binario ==================================
#=============================================================================



def Bin_Dec(Bin):
	#~ Binario a Decimal
	
	lista = []
	xD = ""
	
	for num in Bin:
		if num != " ":
			xD = xD + num
		else:
			xD = int(xD, 2)
			lista.append(xD)
			xD = ""
	xD = int(xD, 2)
	lista.append(xD)
	
	print("\n\n [+] Decimal >> ", end='')
	
	for Dec in lista:
		print(Dec, end=' ')
	
	print("\n\n")



#=============================================================================
#==================================== x=D ====================================
#=============================================================================

#~ Para Pruebas:
Hex = "68 6f 6c 61"
Asc = "hola"
Dec = "104 111 108 97"
#~ Bin = "01101000 01101111 01101100 01100001"

while True:
	Bin = input(" [+] Binario: ")
	Dec = Bin_Dec(Bin)
#~ print("\n\n [*] Ascii: \n\n >> " + Asc + "\n\n\n --> Convertido <--\n\n\n [+] Decimal: \n\n >> " + Dec)
