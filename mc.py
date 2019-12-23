# Takes Arguments:
import sys

File = open("c:/Users/XXX/AppleShortcuts/action.txt", "r+")
File.write(f"mc\n{sys.argv[1]}")
File.close()