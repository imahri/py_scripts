import pyperclip
import subprocess

try:
    src = input(">> ")
    src = src.upper()
    pyperclip.copy(src)
    print("Done")

except KeyboardInterrupt:
    print("\nExecution interrupted by Ctrl + C")
    # subprocess.run('deactivate', shell=True)
    # print("thanks")