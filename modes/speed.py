import os
import sys
import colorama as color
color.init()
path = os.getenv('PATH').split(';')
end = color.Style.RESET_ALL + "\n"

rmAudio = False

inputFile = input("Input file: ")
speed = input("Video Speed: ")
newFPS = input("New FPS: ")
audioProm = input("Remove Audio? (y/N): ")
if audioProm.lower() == "y": rmAudio = True
detectError = False
sampleRate = 0
sampleConfirm = ""
if not rmAudio:
    try:
        os.system(f"ffmpeg -i \"{inputFile}\" 2> temp.txt")
        with open("temp.txt", "r") as audioInfo:
            sampleRate = audioInfo.read().split(" Hz, ")[0].split(" ")[-1]
        os.remove("temp.txt")
        sampleConfirm = input("Detected Sample Rate: " + sampleRate + "\nIs this correct? (Y/n): ")
    except:
        print("An error occurred while trying to detect Sample rate.")
        detectError = True
    if sampleConfirm.lower() == "n" or detectError: sampleRate = input("Audio Sample Rate: ")
outputFile = input("Output file: ")

print(f"\n{color.Fore.CYAN}Please choose a codec to use:", end=end)
print(f"lib{color.Fore.GREEN}x{color.Fore.RESET}264 - CPU Encoding")
print(f"h264_{color.Fore.GREEN}n{color.Fore.RESET}venc - NVIDIA GPU Encoding")
print(f"h264_{color.Fore.GREEN}a{color.Fore.RESET}mf - AMD GPU Encoding")
print(f"{color.Fore.GREEN}O{color.Fore.RESET}ther", end="\n\n")

codecChoice = ""
correctCodec = False
while not correctCodec:
    codecChoice = input("> ").lower()
    correctCodec = True
    if codecChoice == "x": codec = "libx264"
    elif codecChoice == "n": codec = "h264_nvenc"
    elif codecChoice == "a": codec = "h264_amf"
    elif codecChoice == "o":
        codec = input("Codec name: ")
    else: print(color.Fore.RED + "Invalid choice", end=end);correctCodec = False

print(color.Fore.YELLOW+"\nMake sure you entered these correctly!", end=end)
print("Input File: " + inputFile)
if not rmAudio: print("Sample Rate: " + sampleRate)
print("Video Speed: " + speed)
print("New FPS: " + newFPS)
print("Output File: " + outputFile)
print("Codec: " + codec)
confirmConvert = input("Start conversion? (Y/n): ")
if confirmConvert.lower() == "n": sys.exit()
print("Starting conversion...")
if rmAudio:
    with open ("temp.txt", "w") as f:
        f.write(f"ffmpeg -i \"{inputFile}\" -c:v {codec} -filter_complex \"[0:v]setpts=PTS/{speed}[v]\" -map \"[v]\" -r {newFPS} \"{outputFile}\"\n{outputFile}")
if not rmAudio:
    with open("temp.txt", "w") as f:
        f.write(f"ffmpeg -i \"{inputFile}\" -c:v {codec} -filter_complex \"[0:v]setpts=PTS/{speed}[v];[0:a]asetrate={sampleRate}*{speed}[a]\" -map \"[v]\" -map \"[a]\" -r {newFPS} \"{outputFile}\"\n{outputFile}")