import random
import string
import os
import colorama
from colorama import Fore
code = "20"


def Home():
  os.system('cls')
  print(f'''
  {Fore.BLUE} _  _ _ _               _____            
  {Fore.BLUE} | \ | (_) |             |  __ \           
  {Fore.BLUE} |  \| |_| |_ _ __ ___   | |  \/ ___ _ __  
  {Fore.BLUE} | . ` | | __| '__/ _ \  | | __ / _ \ '_ \ 
  {Fore.BLUE} | |\  | | |_| | | (_) | | |_\ \  __/ | | |
  {Fore.BLUE} \_| \_/_|\__|_|  \___/   \____/\___|_| |_| 
  {Fore.BLUE}      
  {Fore.BLUE}        by discord.gg/tool
  {Fore.BLUE}        [1] Nitro Gen                 
  {Fore.BLUE}        
  {Fore.BLUE}
  ''')
  x = int(input(">>"))
  if x == 1:
    Nitro()

def Code():
  letters = string.ascii_letters + string.digits
  return ''.join(random.choice(letters) for i in range(19))

  
def Nitro():
  global code
  code = Code()
  f = open("nitros.txt", "w") 
  b = int(input("How many nitros you want to generate?>>"))
  for times in range(b):
    f.write(f"discord.gift/")
    f.write(f"{code}")
    f.write("\n")
    code = Code()
    print(f"{Fore.GREEN}NITRO [+] {Fore.BLUE}discord.gift/{code}")
Home()


   

Home()
Loader()
