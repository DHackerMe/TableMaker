import platform; import os

def title(): print(" _____     _     _      __  __       _\n|_   ___ _| |__ | | ___|  \/  |v1.1_| |_by_DHMe__\n  | |/ _` | '_ \| |/ _ | |\/| |/ _` | |/ / _ | '__|\n  | | (_| | |_) | |  __| |  | | (_| |   |  __| |\n  |_|\__,_|_.__/|_|\___|_|  |_|\__,_|_|\_\___|_|\n")

if platform.system() == "Windows":
  def clear(): os.system("cls")
else:
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

if tr == 0:
  clear()
  title()
  print("Nothing to consider.")
  exit()

tab += "\n"+"-"*tr
clear()

while True:
  
  title()
  while name != N:
    name = input("Input the Name: ")
    if len(name) <= 15:
      break
    print("Name too long.")
  clear()

  title()
  while surname != N:
    surname = input("Input the Surname: ")
    if len(surname) <= 15:
      break
    print("Surname too long.")
  clear()

  title()
  while age != N:
    age = int(input("Input the age: "))
    if age > 0 and age < 120:
      break
    print("Input a valid age.")
  clear()

  title()
  tab += "\n"
  if name != N: tab += (name+" "*(16-len(name)))
  if surname != N: tab += (surname+" "*(16-len(surname)))
  if age != N: tab += (str(age)+" "*(3-len(str(age))))
  if input("Repeat? (Y/n): ").upper() == "N":
    break
  tab += "\n"
  clear()

clear()
title()
print(tab)
