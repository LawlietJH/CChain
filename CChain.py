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
#                                                              v1.0.6

import os
import sys

Autor = "LawlietJH"
Version = "v1.0.6"

#=============================================================================
#================================ Hexadecimal ================================
#=============================================================================


def Hex_Asc(Hex):
	#~ Hexadecimal a Ascii
	
	Hex = Hex.replace(" ", "")

	Ascii = ''.join((chr(int(Hex[i:i+2], 16)) for i in range(0, len(Hex), 2)))
	
	return Ascii



def Hex_Bin(Hex):
	#~ Hexadecimal a Binario.
	
	cont = 0
	Cadena = ""
	Hex = Hex.replace(" ", "")

	Bin = ''.join((bin(int(Hex[i:i+2], 16))[2:].zfill(8) for i in range(0, len(Hex), 2)))
	
	#~ Se separa la cadena con un espacio en cada byte.
	for b in Bin:
		cont += 1
		if(cont <= 7):
			Cadena = Cadena + b
		else:
			Cadena = Cadena + b + " "
			cont = 0
	
	return Cadena



def Hex_Dec(Hex):
	#~ Hexadecimal a Decimal.
	
	xD = ""
	cont = 0
	lista = []
	Decimal = ""
	
	Hex = Hex.upper()				#~ Pone Todo En Mayusculas.
	Hex = Hex.replace(" ", "")		#~ Quita Los Espacios.
	
	for i in Hex:
		cont += 1
		
		if cont % 2 != 0:
			xD = xD + i
		else:
			xD = xD + i
			lista.append(str(eval("0x" + xD)) + " ")
			xD = ""
	
	for Dec in lista:
		Decimal += Dec
	
	return Decimal



#=============================================================================
#=================================== Ascii ===================================
#=============================================================================



def Asc_Hex(Ascii):
	#~ Ascii a Hexadecimal
	
	cont = 0
	Hex = ''.join((hex(ord(c))[2:] for c in Ascii))
	
	print("\n\n [+] Hexadecimal: \n\n >> ", end='')
	
	for x in Hex:
		cont += 1
		if cont % 2 != 0:
			print(x, end='')
		else:
			print(x, end=' ')
	
	print("")



def Asc_Bin():
	pass



def Asc_Dec():
	pass



#=============================================================================
#================================== Decimal ==================================
#=============================================================================



#=============================================================================
#================================== Binario ==================================
#=============================================================================



#=============================================================================
#==================================== x=D ====================================
#=============================================================================

#~ Para Pruebas:
Hex = "68 6f 6c 61"
Asc = "hola"
Dec = "104 111 108 97"
Bin = "01101000 01101111 01101100 01100001"
