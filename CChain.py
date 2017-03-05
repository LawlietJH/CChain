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

import os
import sys

Autor = "LawlietJH"
Version = "v1.0.4"

#=============================================================================
#================================ Hexadecimal ================================
#=============================================================================


def Hex_Ascii(Hex):
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

