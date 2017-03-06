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
#                                                              v1.2.0

import time
import sys
import os

Autor = "LawlietJH"
Version = "v1.2.0"



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



#=============================================================================
#================================== Binario ==================================
#=============================================================================



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
						print("\n\n\t Cadena en Hexadecimal: " + Hex + "\n")
						
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
						print("\n\n\t Cadena en Binario: " + Bin + "\n")
						
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
						print("\n\n\t Cadena en Decimal: " + Dec + "\n")
						
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
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				os.system("cls && title De Hexadecimal a Ascii")
				#~ Hexadecimal a Ascii:

				while True:

					try:
						Hex = input("\n\n\t Cadena Hexadecimal: ")
						Asc = Hex_Asc(Hex)
						print("\n\n\t Cadena en Ascii: " + Asc + "\n")
						
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
						print("\n\n\t Cadena en Binario: " + Bin + "\n")
						
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
						print("\n\n\t Cadena en Decimal: " + Dec + "\n")
						
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
			#~ print("\n\n\t\t 1 - Binario a Ascii.")
			#~ print("\n\t\t 2 - Binario a Hexadecimal.")
			print("\n\t\t 3 - Binario a Decimal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				#~ os.system("cls && title De Binario a Ascii")
				#~ Binario a Ascii:

				#~ while True:

					#~ try:
						#~ Bin = input("\n\n\t Cadena Binaria: ")
						#~ Asc = Bin_Asc(Bin)
						#~ print("\n\n\t Cadena en Ascii: " + Asc + "\n")
						
					#~ except KeyboardInterrupt:			#~ Ctrl+C para volver
						#~ print("\n\n\t Volviendo...")
						#~ time.sleep(0.5)
						#~ break
						
					#~ except:
						#~ print("\n\n Tiene Caracteres No Válidos.")
					pass
								
			elif Opc == "2":
				#~ os.system("cls && title De Binario a Hexadecimal")
				#~ Binario a Hexadecimal:

				#~ while True:

					#~ try:
						#~ Bin = input("\n\n\t Cadena Binaria: ")
						#~ Hex = Bin_Hex(Bin)
						#~ print("\n\n\t Cadena en Hexadecimal: " + Hex + "\n")
						
					#~ except KeyboardInterrupt:			#~ Ctrl+C para volver
						#~ print("\n\n\t Volviendo...")
						#~ time.sleep(0.5)
						#~ break
						
					#~ except:
						#~ print("\n\n Tiene Caracteres No Válidos.")
					pass
					
			elif Opc == "3":
				os.system("cls && title De Binario a Decimal")
				#~ Binario a Decimal:

				while True:

					try:
						Bin = input("\n\n\t Cadena Binaria: ")
						Dec = Bin_Dec(Bin)
						print("\n\n\t Cadena en Decimal: " + Dec + "\n")
						
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
			#~ print("\n\n\t\t 1 - Decimal a Ascii.")
			#~ print("\n\t\t 2 - Decimal a Hexadecimal.")
			print("\n\t\t 3 - Decimal a Binario.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				#~ os.system("cls && title De Decimal a Ascii")
				#~ Decimal a Ascii:

				#~ while True:

					#~ try:
						#~ Dec = input("\n\n\t Cadena Decimal: ")
						#~ Asc = Dec_Asc(Dec)
						#~ print("\n\n\t Cadena en Ascii: " + Asc + "\n")
						
					#~ except KeyboardInterrupt:			#~ Ctrl+C para volver
						#~ print("\n\n\t Volviendo...")
						#~ time.sleep(0.5)
						#~ break
						
					#~ except:
						#~ print("\n\n Tiene Caracteres No Válidos.")
				pass
								
			elif Opc == "2":
				#~ os.system("cls && title De Decimal a Hexadecimal")
				#~ Decimal a Hexadecimal:

				#~ while True:

					#~ try:
						#~ Dec = input("\n\n\t Cadena Decimal: ")
						#~ Hex = Dec_Hex(Dec)
						#~ print("\n\n\t Cadena en Hexadecimal: " + Hex + "\n")
						
					#~ except KeyboardInterrupt:			#~ Ctrl+C para volver
						#~ print("\n\n\t Volviendo...")
						#~ time.sleep(0.5)
						#~ break
						
					#~ except:
						#~ print("\n\n Tiene Caracteres No Válidos.")
				pass
					
			elif Opc == "3":
				os.system("cls && title De Decimal a Binario")
				#~ Binario a Decimal:

				while True:

					try:
						Dec = input("\n\n\t Cadena Decimal: ")
						Bin = Dec_Bin(Dec)
						print("\n\n\t Cadena en Binario: " + Bin + "\n")
						
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
			print("\n\n\t\t 2 - Hexadecimal.")
			print("\n\n\t\t 3 - Binario.")
			print("\n\n\t\t 4 - Decimal.")
			Opc = input("\n\n\t Opción: ")
			
			if Opc == "1":
				
				Asc_Menu()
			
			elif Opc == "2":
				Hex_Menu()
				
			elif Opc == "3":
				Bin_Menu()
				
			elif Opc == "4":
				Dec_Menu()
				
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


