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
        print("Please download it from https://ffmpeg.org", end=end)
if not fileFound: sys.exit()
print(color.Style.BRIGHT + color.Fore.BLUE + "\nMotdHS's FFmpeg Utility v0.0.1 " + color.Style.NORMAL + color.Fore.YELLOW + "WIP", end=end)
print("(1) Change the quality of the video")
print(f"(2) {color.Fore.YELLOW}[SOON]{color.Fore.RESET} Convert .avi to .mp4 and change the quality of the video")
print(f"(3) {color.Fore.YELLOW}[SOON]{color.Fore.RESET} Change the speed of the video", end="\n\n")
validChoice = False
while not validChoice:
    choice = input("> ")
    if choice == "1":
        validChoice = True
    elif choice == "2" or choice == "3" or choice == "4":
        print(color.Fore.YELLOW+"Coming in future versions.", end=end)
choiceInt = int(choice)
if choiceInt == 1:
    print(color.Fore.YELLOW+"Note: You can only use .mp4 as of now.", end=end)
    inputFile = ""
    while not inputFile.endswith(".mp4"):
        inputFile = input("Input file: ")
        if not inputFile.endswith(".mp4"):
            print(color.Fore.RED + "Please enter a .mp4 file.", end=end)
    newBitrate = input("New Bitrate (in kbps): ")
    newFPS = input("New FPS: ")
    newRes = input("New Resolution (ex. 1920x1080): ").split("x")
    outputFile = ""
    while not outputFile.endswith(".mp4"):
        outputFile = input("Output file: ")
        if not outputFile.endswith(".mp4"):
            print(color.Fore.RED + "Please enter a .mp4 file.", end=end)
    print("Please choose a codec to use:")
    print(color.Fore.YELLOW+"\nMake sure you entered these correctly!", end=end)
    confirmConvert = input("Start conversion? (Y/n): ")
    if confirmConvert.lower() == "n": sys.exit()
    print("Starting conversion...")
    os.system(f"ffmpeg -i \"{inputFile}\" -c:v {codec} -s {newRes[0]}x{newRes[1]} -b:v {newBitrate}k -bufsize {newBitrate}k -r {newFPS} \"{outputFile}\"")
    print(color.Fore.GREEN+"Conversion complete!", end=end)
    input("Press enter to exit.")