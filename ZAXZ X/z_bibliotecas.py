try:    
    from colorama import Fore, Style, init
    import time
    import sys 
    import termios
    import csv
    import subprocess
    import pyautogui
    import ipaddress
    import pandas as pd
    from pyfiglet import figlet_format
    init()

except Exception as erro:
    print("\n\nErro ao importar bibliotecas, procure como instalar aa bibliotecas 'colorama', 'pandas', 'pyautogui', 'pyfiglet' de python para prosseguir.\n")
    print(f"\nDetalhes do erro: {erro}\n\n")
    exit()

try:
    def block():
        fd = sys.stdin.fileno()
        novo = termios.tcgetattr(fd)
        novo[3] &= ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, novo)

    def unblock():
        fd = sys.stdin.fileno()
        novo = termios.tcgetattr(fd)
        novo[3] |= termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, novo)

    def ignore():
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

    def dormir(tempo):
        return time.sleep(tempo)

    def print_slow(texto, segundos=0.02):
        for coisa in texto:
            print(coisa, end="", flush=True)
            dormir(segundos)
        print(Style.RESET_ALL)

    def input_slow(texto, segundos=0.03):
        for coisa in texto:
            print(coisa, end="", flush=True)
            dormir(segundos)
        print(Style.RESET_ALL, end="")
        unblock()
        ignore()
        inputar = input()
        block()
        return inputar

    def verde():
        return Fore.GREEN + Style.BRIGHT

    def amarelo():
        return Fore.YELLOW + Style.BRIGHT

    def vermelho():
        return Fore.RED + Style.BRIGHT

    def roxo():
        return Fore.MAGENTA + Style.BRIGHT

    def branco():
        return Fore.WHITE + Style.BRIGHT

    def azul():
        return Fore.BLUE + Style.BRIGHT
    
except Exception as erro:
    print("\n\nErro ao montar base padrão para o funcionamento do sistema, você modificou o código?\n")
    print(f"\nDetalhes do erro: {erro}\n\n")
    exit()
