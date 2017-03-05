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
Version = "v1.0.2"

#=============================================================================
#================================ Hexadecimal ================================
#=============================================================================


def Hex_Ascii(Hex):
	#~ Hexadecimal a Ascii
	
	Hex = Hex.replace(" ", "")

	Ascii = ''.join((chr(int(Hex[i:i+2], 16)) for i in range(0, len(Hex), 2)))
	
	print("\n\n [+] Ascii: \n\n >> "+Ascii)



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
	
	print("\n\n [+] Binario: \n\n >> "+Cadena)


#=============================================================================
#=============================================================================
#=============================================================================
