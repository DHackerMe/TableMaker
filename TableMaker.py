import os

def title(): print(" _____     _     _      __  __       _\n|_   ___ _| |__ | | ___|  \/  | __ _| |_____ _ __\n  | |/ _` | '_ \| |/ _ | |\/| |/ _` | |/ / _ | '__|\n  | | (_| | |_) | |  __| |  | | (_| |   |  __| |\n  |_|\__,_|_.__/|_|\___|_|  |_|\__,_|_|\_\___|_|\n")

def clear(): os.system("clear")

tab = ""; tr = 0
N = "00000000000000000000"

clear()
title()
if input("Consider Name? (Y/n): ").upper() == "N": name = N
else:
  tab += "NAME            "
  name = ""
  tr += 16
if input("Consider Surname? (Y/n): ").upper() == "N": surname = N
else:
  tab += "SURNAME         "
  surname = ""
  tr += 16
if input("Consider Age? (Y/n): ").upper() == "N": age = N
else:
  tab += "AGE"
  age = ""
  tr += 3

if tab == 0:
  clear()
  title()
  print("Nothing to consider.")
  exit()

tab += "\n"+"-"*tr
clear()

while True:

  while name != N:
    title()
    name = input("Input the Name: ")
    if len(name) <= 15:
      break
    print("Name too long.")
  clear()
  
  while surname != N:
    title()
    surname = input("Input the Surname: ")
    if len(surname) <= 15:
      break
    print("Surname too long.")
  clear()
  
  while age != N:
    title()
    age = input("Input the age: ")
    if int(age) > 0 or int(age) < 120:
      break
    print("Input a valid age.")
  clear()

  title()
  tab += "\n"
  if name != N: tab += (name+" "*(16-len(name)))
  if surname != N: tab += (surname+" "*(16-len(surname)))
  if age != N: tab += (age+" "*(3-len(age)))
  if input("Repeat? (Y/n): ").upper() == "N":
    break
  tab += "\n"
  clear()

clear()
title()
print(tab)
