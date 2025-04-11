import requests
import os
import random
import string
import time
from colorama import Fore, Style, init

init(autoreset=True)

# @Ilzci
logo =logo = r"""
           ______
        .-        -.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \o_)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
         
     Made By Black Beard
"""

# Made By Black Beard
def loading_effect():
    print(Fore.YELLOW + "  [*] Please wait...")
    for _ in range(3):
        print(Fore.YELLOW + ". ", end="")
        time.sleep(0.5)
    print()

def generate_from_wordlist(num_passwords, save_path):
    print(Fore.CYAN + "  [*] Downloading wordlist...")
    loading_effect()
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt"
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(save_path, "wordlist.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            lines = response.text.splitlines()[:num_passwords]
            f.write("\n".join(lines))
        print(Fore.GREEN + f"\n  [+] Saved successfully at: {file_path}")
    else:
        print(Fore.RED + "  [!] Failed to download wordlist.")

def generate_random_passwords(count, length, use_upper, use_digits, use_symbols, save_path):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    file_path = os.path.join(save_path, "wordlist.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(count):
            password = ''.join(random.choice(chars) for _ in range(length))
            f.write(password + "\n")
    print(Fore.GREEN + f"\n  [+] Random passwords saved at: {file_path}")

def main():
    print(Fore.CYAN + Style.BRIGHT + logo)
    print(Fore.YELLOW + "  [1] Generate from leaked wordlist (rockyou)")
    print("  [2] Generate random passwords")
    
    choice = input(Fore.CYAN + "\n  [~] Choose an option (1 or 2): ").strip()

    if choice not in ['1', '2']:
        print(Fore.RED + "  [!] Invalid choice.")
        return

    save_path = input(Fore.YELLOW + "  [~] Enter full path to save the file: \n ").strip()
    if not os.path.exists(save_path):
        print(Fore.RED + "  [!] The folder does not exist.")
        return

    if choice == '1':
        try:
            num_passwords = int(input(Fore.YELLOW + "  [~] Number of passwords to download: "))
            generate_from_wordlist(num_passwords, save_path)
        except ValueError:
            print(Fore.RED + "  [!] Invalid number.")
    
    elif choice == '2':
        try:
            count = int(input(Fore.YELLOW + "  [~] Number of passwords to generate: "))
            length = int(input("  [~] Length of each password: "))
            use_upper = input("  [~] Include UPPERCASE letters? (y/n): ").lower() == 'y'
            use_digits = input("  [~] Include digits? (y/n): ").lower() == 'y'
            use_symbols = input("  [~] Include symbols? (y/n): ").lower() == 'y'

            generate_random_passwords(count, length, use_upper, use_digits, use_symbols, save_path)
        except ValueError:
            print(Fore.RED + "  [!] Invalid input.")

    print(Fore.MAGENTA + Style.BRIGHT + "\n   Done by Black Beard  |  @Ilzci\n")

if __name__ == "__main__":
    main()