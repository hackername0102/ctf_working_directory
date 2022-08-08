#!/usr/bin/python3
import sys
import os
from termcolor import colored


def usage():
    print(colored(f"[*] Usage: python3 {sys.argv[0]} [dir of ctf platform] [challenge name]", "red"))

def create_dir(dir, dir_name):
    try:
        os.mkdir(f"{dir}/{dir_name}")                   # creating directory
        return True                                     # positive result
    except:
        return False                                    # negative result

def main():
    dirs = ["nmap", "dirs", "exploits"]                 # dirs to create
    
    working_dir = create_dir(sys.argv[1], sys.argv[2])              # working directory
    if working_dir == True:
        print(colored(f"[+] created {sys.argv[1]}/{sys.argv[2]}", "green"))
        for dir in dirs:                            # creating dirs from list
            create_dir(sys.argv[1], f"{sys.argv[2]}/{dir}")             # creating dir
            print(colored(f"[+] created {sys.argv[1]}/{sys.argv[2]}/{dir}", "green"))

    else:
        print(colored("[-] some error occurred", "red"))
        sys.exit()

if __name__ == "__main__":
    if os.getlogin() == "root":
        if len(sys.argv) == 3:
            main()
        else:
            usage()
    else:
        print(colored("[-] execute script as root", "red"))