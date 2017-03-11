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
#                                                              v1.3.6

import time
import sys
import os

Autor = "LawlietJH"
Version = "v1.3.6"



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
	
	Hexadecimal = Hexadecimal.upper()
	
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



def Hex_Oct(Hex):	#~ Hexadecimal a Octal.
	
	Oct = int(Hex, 16)
	Oct = str(oct(Oct))
	Octal = Oct[2:]
	
	return Octal



#=============================================================================
#================================== Binario ==================================
#=============================================================================




def Bin_Asc(Bin):	#~ Binario a Ascii

	Bin = Bin.replace(" ", "")	#~ Remplaza Los espacios por Cadena Vacia.

	Ascii = ''.join((chr(int(Bin[i:i+8], 2)) for i in range(0, len(Bin), 8)))
	
	return Ascii



def Bin_Hex(Bin):	#~ Binario a Hexadecimal
	
	xD = ""
	Lista = []
	Hexadecimal = ""
		
	for Hex in Bin:
		
		if Hex != " ":
			xD = xD + Hex
		
		else:
			xD = "".join((hex(int(xD[i:i+8], 2))[2:] for i in range(0, len(xD), 8)))
			Lista.append(xD+" ")
			xD = ""
	
	xD = "".join((hex(int(xD[i:i+8], 2))[2:] for i in range(0, len(xD), 8)))
	Lista.append(xD)
	
	for Hex in Lista:
		
		Hexadecimal += Hex
	
	Hexadecimal = Hexadecimal.upper()
	
	return Hexadecimal



def Bin_Dec(Bin):	#~ Binario a Decimal
	
	xD = ""
	Lista = []
	Decimal = ""
	
	#~ Se toma cada Byte y se Almacena en Lista para su Posterior conversión.
	for Num in Bin:
		
		if Num != " ":
			xD = xD + Num
			
		else:
			xD = int(xD, 2)
			Lista.append(xD)
			xD = ""
	
	xD = int(xD, 2)
	Lista.append(xD)
	
	for Dec in Lista:			#~ Se Añade Cada Número a la Cadena.
		Decimal += str(Dec) + " "
	
	return Decimal



def Bin_Oct(Bin):	#~ Binario a Octal.
	
	Oct = int(Bin, 2)
	Oct = oct(Oct)
	Oct = str(Oct)
	Oct = Oct[2:]
	
	return Oct




#=============================================================================
#================================== Decimal ==================================
#=============================================================================



def Dec_Asc(Dec):	#~ Decimal a Ascii.
	
	xD = ""
	Ascii = ""
	Lista = []
	
	for num in Dec:
		
		if num != " ":
			xD = xD + num
		
		else:
			Lista.append(chr(int(xD)))
			xD = ""
			
	Lista.append(chr(int(xD)))
	
	for Asc in Lista:
		
		Ascii += Asc	
	
	return Ascii



def Dec_Hex(Dec):	#~ Decimal a Hexadecimal.
	
	xD = ""
	Lista = []
	Hexadecimal = ""
	
	for Hex in Dec:
		
		if Hex != " ":
			xD = xD + Hex
		
		else:
			xD = hex(int(xD)).split('x')[1]
			Lista.append(xD+" ")
			xD = ""
	
	xD = hex(int(xD)).split('x')[1]
	Lista.append(xD)
	
	for Hexa in Lista:
		
		Hexadecimal += Hexa
	
	Hexadecimal = Hexadecimal.upper()
	
	return Hexadecimal



def Dec_Bin(Dec):	#~ Decimal a Binario.
	
	xD = ""
	Lista = []
	Lista2 = []
	Binario = ""

	#~ Se toma cada caracter hasta que encuentre un espacio
	#~ y esta cadena se agrega a una lista para convertir posteriormente.
	for Num in Dec:
		
		if Num != " ":
			xD = xD + Num
		else:
			xD = bin(int(xD))
			Lista.append(xD[2:])
			xD = ""
			
	xD = bin(int(xD))
	Lista.append(xD[2:])
	
	#~ Se Añaden los 0 Faltantes al Inicio.
	for Bin in Lista:
		
		xD = Bin
		
		while True:
		
			if len(xD) % 8 != 0:
				xD = "0" + xD
				
			else: 
				Lista2.append(xD)
				break
	
	for Bin in Lista2:			#~ Se Añaden los Bytes a La Cadena.
		Binario += Bin + " "
	
	return Binario



def Dec_Oct(Dec):	#~ Decimal a Octal.
	
	Numero = int(Dec)
	Octal = oct(Numero)
	Octal = Octal[2:]
	Octal = str(Octal)
	
	return Octal



#=============================================================================
#==================================== Octal ==================================
#=============================================================================



def Oct_Hex(Oct):	#~ Octal a Hexadecimal.
	
	Hex = int(Oct, 8)
	Hex = hex(Hex)
	Hexadecimal = Hex[2:]
	
	return Hexadecimal



def Oct_Bin(Oct):	#~ Octal a Binario.
	
	Binario = int(Oct, 8)
	Binario = bin(Binario)
	Binario = Binario[2:]
	
	return Binario



def Oct_Dec(Oct):	#~ Octal a Decimal.
	
	Decimal = str(int(Oct, 8))
	
	return Decimal



#~ https://codescracker.com/python/program/python-program-convert-octal-to-hexadecimal.htm
#=============================================================================
#================================== Menú Asc =================================
#=============================================================================



def Asc_Menu():
	
	while True:
		
		try:
			os.system("cls && title Ascii Menú")
			print("\n\n\t\t 1 - Ascii a Hexadecimal.")
			print("\n\t\t 2 - Ascii a Binario.")
			print("\n\t\t 3 - Ascii a Decimal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				os.system("cls && title De Ascii a Hexadecimal")
				#~ Ascii a Hexadecimal:

				while True:

					try:
						Asc = input("\n\n\t Cadena Ascii: ")
						Hex = Asc_Hex(Asc)
						print("\n\t Cadena en Hexadecimal: " + Hex + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "2":
				os.system("cls && title De Ascii a Binario")
				#~ Ascii a Binario:

				while True:

					try:
						Asc = input("\n\n\t Cadena Ascii: ")
						Bin = Asc_Bin(Asc)
						print("\n\t Cadena en Binario: " + Bin + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "3":
				os.system("cls && title De Ascii a Decimal")
				#~ Ascii a Decimal:

				while True:

					try:
						Asc = input("\n\n\t Cadena Ascii: ")
						Dec = Asc_Dec(Asc)
						print("\n\t Cadena en Decimal: " + Dec + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			else:
				print("\n\n\t\t Opción no válida...")
				time.sleep(0.5)
				
		except KeyboardInterrupt:			#~ Ctrl+C para volver
			print("\n\n\t Volviendo...")
			time.sleep(0.5)
			break
			



#=============================================================================
#================================== Menú Hex =================================
#=============================================================================



def Hex_Menu():
	
	while True:
		
		try:
			os.system("cls && title Hexadecimal Menú")
			print("\n\n\t\t 1 - Hexadecimal a Ascii.")
			print("\n\t\t 2 - Hexadecimal a Binario.")
			print("\n\t\t 3 - Hexadecimal a Decimal.")
			print("\n\t\t 4 - Hexadecimal a Octal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				os.system("cls && title De Hexadecimal a Ascii")
				#~ Hexadecimal a Ascii:

				while True:

					try:
						Hex = input("\n\n\t Cadena Hexadecimal: ")
						Asc = Hex_Asc(Hex)
						print("\n\t Cadena en Ascii: " + Asc + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "2":
				os.system("cls && title De Hexadecimal a Binario")
				#~ Hexadecimal a Binario:

				while True:

					try:
						Hex = input("\n\n\t Cadena Hexadecimal: ")
						Bin = Hex_Bin(Hex)
						print("\n\t Cadena en Binario: " + Bin + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "3":
				os.system("cls && title De Hexadecimal a Decimal")
				#~ Hexadecimal a Decimal:
			
				while True:
			
					try:
						Hex = input("\n\n\t Cadena Hexadecimal: ")
						Dec = Hex_Dec(Hex)
						print("\n\t Cadena en Decimal: " + Dec + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "4":
				os.system("cls && title De Hexadecimal a Octal")
				#~ Hexadecimal a Octal:
			
				while True:
			
					try:
						Hex = input("\n\n\t Cadena Hexadecimal: ")
						Oct = Hex_Oct(Hex)
						print("\n\t Cadena en Octal: " + Oct + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			else:
				print("\n\n\t\t Opción no válida...")
				time.sleep(0.5)
				
		except KeyboardInterrupt:			#~ Ctrl+C para volver
			print("\n\n\t Volviendo...")
			time.sleep(0.5)
			break
			


#=============================================================================
#================================== Menú Bin =================================
#=============================================================================



def Bin_Menu():
	
	while True:
		
		try:
			os.system("cls && title Binario Menú")
			print("\n\n\t\t 1 - Binario a Ascii.")
			print("\n\t\t 2 - Binario a Hexadecimal.")
			print("\n\t\t 3 - Binario a Decimal.")
			print("\n\t\t 4 - Binario a Octal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				os.system("cls && title De Binario a Ascii")
				#~ Binario a Ascii:

				while True:

					try:
						Bin = input("\n\n\t Cadena Binaria: ")
						Asc = Bin_Asc(Bin)
						print("\n\t Cadena en Ascii: " + Asc + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
								
			elif Opc == "2":
				os.system("cls && title De Binario a Hexadecimal")
				#~ Binario a Hexadecimal:

				while True:

					try:
						Bin = input("\n\n\t Cadena Binaria: ")
						Hex = Bin_Hex(Bin)
						print("\n\t Cadena en Hexadecimal: " + Hex + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
					
			elif Opc == "3":
				os.system("cls && title De Binario a Decimal")
				#~ Binario a Decimal:

				while True:

					try:
						Bin = input("\n\n\t Cadena Binaria: ")
						Dec = Bin_Dec(Bin)
						print("\n\t Cadena en Decimal: " + Dec + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "4":
				os.system("cls && title De Binario a Octal")
				#~ Binario a Octal:

				while True:

					try:
						Bin = input("\n\n\t Cadena Binaria: ")
						Oct = Bin_Oct(Bin)
						print("\n\t Cadena en Octal: " + Oct + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			else:
				print("\n\n\t\t Opción no válida...")
				time.sleep(0.5)
				
		except KeyboardInterrupt:			#~ Ctrl+C para volver
			print("\n\n\t Volviendo...")
			time.sleep(0.5)
			break
			


#=============================================================================
#================================== Menú Dec =================================
#=============================================================================



def Dec_Menu():
	
	while True:
		
		try:
			os.system("cls && title Decimal Menú")
			print("\n\n\t\t 1 - Decimal a Ascii.")
			print("\n\t\t 2 - Decimal a Hexadecimal.")
			print("\n\t\t 3 - Decimal a Binario.")
			print("\n\t\t 4 - Decimal a Octal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				os.system("cls && title De Decimal a Ascii")
				#~ Decimal a Ascii:

				while True:

					try:
						Dec = input("\n\n\t Cadena Decimal: ")
						Asc = Dec_Asc(Dec)
						print("\n\t Cadena en Ascii: " + Asc + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
								
			elif Opc == "2":
				os.system("cls && title De Decimal a Hexadecimal")
				#~ Decimal a Hexadecimal:

				while True:

					try:
						Dec = input("\n\n\t Cadena Decimal: ")
						Hex = Dec_Hex(Dec)
						print("\n\t Cadena en Hexadecimal: " + Hex + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
					
			elif Opc == "3":
				os.system("cls && title De Decimal a Binario")
				#~ Binario a Decimal:

				while True:

					try:
						Dec = input("\n\n\t Cadena Decimal: ")
						Bin = Dec_Bin(Dec)
						print("\n\t Cadena en Binario: " + Bin + "\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			elif Opc == "4":
				os.system("cls && title De Decimal a Octal")
				#~ Decimal a Octal:

				while True:

					try:
						Dec = input("\n\n\t Cadena Decimal: ")
						Oct = Dec_Oct(Dec)
						print("\n\t Cadena en Octal: " + Oct + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
			
			else:
				print("\n\n\t\t Opción no válida...")
				time.sleep(0.5)
				
		except KeyboardInterrupt:			#~ Ctrl+C para volver
			print("\n\n\t Volviendo...")
			time.sleep(0.5)
			break
			


#=============================================================================
#================================== Menú Oct =================================
#=============================================================================



def Oct_Menu():
	
	while True:
		
		try:
			os.system("cls && title Octal Menú")
			print("\n\n\t\t 1 - Octal a Hexadecimal.")
			print("\n\t\t 2 - Octal a Binario.")
			print("\n\t\t 3 - Octal a Decimal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				os.system("cls && title De Octal a Hexadecimal")
				#~ Octal a Hexadecimal:

				while True:

					try:
						Oct = input("\n\n\t Cadena Octal: ")
						Hex = Oct_Hex(Oct)
						print("\n\t Cadena en Hexadecimal: " + Hex + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
								
			elif Opc == "2":
				os.system("cls && title De Octal a Binario")
				#~ Octal a Binario:

				while True:

					try:
						Oct = input("\n\n\t Cadena Octal: ")
						Bin = Oct_Bin(Oct)
						print("\n\t Cadena en Binario: " + Bin + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
								
			elif Opc == "3":
				os.system("cls && title De Octal a Decimal")
				#~ Octal a Decimal:

				while True:

					try:
						Oct = input("\n\n\t Cadena Octal: ")
						Dec = Oct_Dec(Oct)
						print("\n\t Cadena en Decimal: " + Dec + "\n\n")
						
					except KeyboardInterrupt:			#~ Ctrl+C para volver
						print("\n\n\t Volviendo...")
						time.sleep(0.5)
						break
						
					except:
						print("\n\n Tiene Caracteres No Válidos.")
								
			else:
				print("\n\n\t\t Opción no válida...")
				time.sleep(0.5)
				
		except KeyboardInterrupt:			#~ Ctrl+C para volver
			print("\n\n\t Volviendo...")
			time.sleep(0.5)
			break
	
	
	
#=============================================================================
#=============================== Menú Principal ==============================
#=============================================================================



def main():
	
	while True:
		
		try:
			os.system("cls && title CChain.py        \
			by:  LawlietJH")
			print("\n\n\t\t 1 - Ascii.")
			print("\n\t\t 2 - Hexadecimal.")
			print("\n\t\t 3 - Binario.")
			print("\n\t\t 4 - Decimal.")
			print("\n\t\t 5 - Octal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				
				Asc_Menu()
			
			elif Opc == "2":
				Hex_Menu()
				
			elif Opc == "3":
				Bin_Menu()
				
			elif Opc == "4":
				Dec_Menu()
				
			elif Opc == "5":
				Oct_Menu()
				
			else:
				print("\n\n\t\t Opción no válida...")
				time.sleep(0.5)
				
		except:
			print("\n\n\t Bye...")
			time.sleep(1)
			exit(0)



#=============================================================================
#==================================== xD =====================================
#=============================================================================



main()


