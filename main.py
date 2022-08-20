version = "0.0.1.1"
import os
import sys
import colorama as color
color.init()
path = os.getenv('PATH').split(';')
fileFound = False
end = color.Style.RESET_ALL + "\n"
os.system('cls')
for curPath in path:
    try:
        with open(f"{curPath}\\ffmpeg.exe", "r") as file:
            fileFound = True
            print(f"{color.Fore.GREEN}FFmpeg detected in PATH", end=end)
    except FileNotFoundError:
        print(end="")
    try:
        with open(f"{curPath}ffmpeg.exe", "r") as file:
            fileFound = True
            print(f"{color.Fore.GREEN}FFmpeg detected in PATH", end=end)
    except FileNotFoundError:
        print(end="")
if not fileFound:
    print(f"{color.Fore.YELLOW}FFmpeg not found in PATH", end=end)
    try:
        with open(os.getcwd() + "\\ffmpeg.exe", "r") as file:
            fileFound = True
            print(f"{color.Fore.GREEN}FFmpeg detected in current directory", end=end)
    except FileNotFoundError:
        print(f"{color.Fore.YELLOW}FFmpeg not found in current directory", end=end)
        print("Please download it from https://ffmpeg.org")
if not fileFound: input("Press enter to exit.");sys.exit()
print(color.Style.BRIGHT + color.Fore.CYAN + "\nMotdHS's FFmpeg Utility v" + version, end=end)
print(color.Fore.RED + "This is not a finished program. If you encounter any bugs, please create an issue on GitHub.", end=end)
print("(1) Change the quality of the video")
print(f"(2) Change the speed of the video")
print(f"(3) {color.Fore.YELLOW}[SOON]{color.Fore.RESET} Change the quality of an audio file, or the audio of a video file")
print()
validChoice = False
while not validChoice:
    choice = input("> ")
    if choice == "1" or choice == "2":
        validChoice = True
    elif choice == "3":
        print(color.Fore.YELLOW+"Coming in future versions.", end=end)
choiceInt = int(choice)
if choiceInt == 1:
    import modes.qual
elif choiceInt == 2:
    import modes.speed
com = ""
try:
    with open("temp.txt", "r") as fif:
        com = fif.read().split("\n")
except FileNotFoundError:
    print("idk how this error is possible but i guess some program is deleting temp.txt")
os.remove("temp.txt")
os.system(com[0])
print("Verifying if the conversion is successful...")
try:
    with open(com[1], "r"):
        print(color.Fore.GREEN+"Conversion complete!", end=end)
except FileNotFoundError:
    print(color.Fore.RED + "Conversion failed! Please try again.", end=end)
except:
    print("Unknown error occurred while checking")
input("Press enter to exit.")
sys.exit()
