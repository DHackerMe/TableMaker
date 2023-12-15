import platform, os, glob, random, subprocess, time,  pandas as pd #time and subprocess for def pandas

def pandas(): #Check if pandas is installed
    print("checking if pandas is installed...")
    time.sleep(3)
    try:
        import pandas as pd
        print("Pandas is installed!")
        print("Enjoy :D")
        time.sleep(3)
    except ImportError:
        install_pandas = input("Pandas is not installed. Do you want to install it now? (y/n): ")
        if install_pandas.lower() == 'y':
            try:
                subprocess.check_call(['pip', 'install', 'pandas'])
                print("Pandas has been installed successfully!")
            except subprocess.CalledProcessError:
                print("Error installing Pandas. Make sure you have pip installed.")
        else:
            print("Pandas installation cancelled.")
def bye():
    print(random.choice(["Bye!", "Goodbye!", "Take care!", "See you soon!", "Until next time!"])) #Farewell is not very friendly

def title():
    print(" _____     _     _      __  __       _\n|_   ___ _| |__ | | ___|  \/  |v2.0d| |_by_DHMe__\n  | |/ _` | '_ \| |/ _ | |\/| |/ _` | |/ / _ | '__|\n  | | (_| | |_) | |  __| |  | | (_| |   |  __| |\n  |_|\__,_|_.__/|_|\___|_|  |_|\__,_|_|\_\___|_|\n")

if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")

def inpt(text):
    try: return input(text)
    except KeyboardInterrupt: clear(); title(); bye(); exit()

def list():
    clear()
    title()

    csv_files = glob.glob("*.csv")

    if not csv_files:
        print("No CSV files found in the current directory.")
    else:
        print("List of CSV files in the current directory:\n")
        for i, file in enumerate(csv_files, start=1):
            print(f"{i}. {file}")

def new_table():
    name = inpt("Input the Name: ")
    surname = inpt("Input the Surname: ")
    age = inpt("Input the age: ")
    
    return name, surname, age

pandas() #Calling the function "pandas" only one time

while True:
    clear()
    title()
    choice = inpt("Menu:\n[1] Create a new CSV file\n[2] List existing CSV files\n[3] Read an existing CSV file\n[4] Modify an existing CSV file\n ")

    if choice == "1":
        data = {"Name": [], "Surname": [], "Age": []}
        
        repeat = "Y"
        while repeat != "N":
            clear()
            title()
            n, s, a = new_table()
            data["Name"].append(n)
            data["Surname"].append(s)
            data["Age"].append(a)
            
            repeat = inpt("Input another? (Y/n): ").upper()
        
        clear()
        title()
        
        filename = inpt("Enter the name to save the CSV file: ")
        file_path = os.path.abspath(filename) #file path
    
        if not filename.lower().endswith('.csv'): filename += '.csv'

        df = pd.DataFrame(data)
    
        df.to_csv(filename, index=False)

        print(f"The file {filename} is saved at: {file_path}") #File name and file path

        print("NAME----------------SURNAME----------------AGE") #Organized List
        for n, s, a in zip(data["Name"], data["Surname"], data["Age"]):
            print(f"{n.ljust(20)}{s.ljust(20)}{a.rjust(6)}")
        inpt("\nPress Enter to continue...")
    
    if choice == "2":
        try: 
            list()
            inpt("\nPress Enter to continue...")
        except Exception as e:
            clear()
            title()
            print(f"An error occurred: {e}")
            inpt("Press Enter to continue...")

    elif choice == "3":
        try:
            list()
            
            filename = inpt("\nEnter the CSV file name: ")

            if not filename.lower().endswith('.csv'): filename += '.csv'

            df = pd.read_csv(filename)

            clear()
            title()
            print("Contents of the CSV file:\n")
            print(df)

            inpt("\nPress Enter to continue...")

        except FileNotFoundError:
            clear()
            title()
            print(f"File '{filename}' not found. Make sure the file exists.")
            inpt("Press Enter to continue...")
        except pd.errors.EmptyDataError:
            clear()
            title()
            print(f"File '{filename}' is empty.")
            inpt("Press Enter to continue...")
        except Exception as e:
            clear()
            title()
            print(f"An error occurred: {e}")
            inpt("Press Enter to continue...")

    elif choice == "4":
        try:
            list()
            
            filename = inpt("\nEnter the CSV file name to modify: ")

            if not filename.lower().endswith('.csv'): filename += '.csv'

            df = pd.read_csv(filename)

            clear()
            title()
            print("Current contents of the CSV file:\n")
            print(df)

            row_index = int(inpt("\nEnter the index of the row to modify: "))

            if row_index < 0 or row_index >= len(df):
                print("Invalid index. Enter a valid index.")
                inpt("Press Enter to continue...")
                continue

            clear()
            title()
            print("Enter new data for the selected row:\n")
            n, s, a = new_table()

            df.loc[row_index] = [n, s, a]

            df.to_csv(filename, index=False)

            clear()
            title()
            print("\nUpdated contents of the CSV file:\n")
            print(df)

            inpt("\nPress Enter to continue...")

        except FileNotFoundError:
            clear()
            title()
            print(f"File '{filename}' not found. Make sure the file exists.")
            inpt("Press Enter to continue...")
        except pd.errors.EmptyDataError:
            clear()
            title()
            print(f"File '{filename}' is empty.")
            inpt("Press Enter to continue...")
        except ValueError:
            clear()
            title()
            print("Invalid input. Enter a valid integer.")
            inpt("Press Enter to continue...")
        except Exception as e:
            clear()
            title()
            print(f"An error occurred: {e}")
            inpt("Press Enter to continue...")
