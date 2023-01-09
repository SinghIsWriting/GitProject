import colorama
from colorama import Fore
colorama.init(autoreset=True)
from random import choice

letters = "abcdefghijklmnopqrstuvwxyz"

def encryptMessage(message):
	encMsg = ""
	for m in message.split():
		if len(m)>=3:
			rand = ""
			for i in range(3):rand = rand+choice(letters)
			m = m + m[0]
			m = rand+m[1:]
			rand = ""
			for i in range(3):rand = rand+choice(letters)
			m = m+rand
			encMsg = encMsg + m + " "
		else:
			encMsg = encMsg + m + " "
	return encMsg

def decryptMessage(encMessage):
	decMsg = ""
	for m in encMessage.split():
		if len(m)>=3:
			m = m[3:-3]
			decMsg = decMsg + m[-1] + m[:-1] + " "
		else:
			decMsg = decMsg + m + " "
	return decMsg

eMsg = encryptMessage(input("Your Message: "))
print(f"\n{Fore.RED}Encrypted Mesaage:", eMsg)
print(f"{Fore.GREEN}Decrypted Message:",decryptMessage(eMsg))
print()
