import os
import sys
import colorama as color
color.init()
path = os.getenv('PATH').split(';')
end = color.Style.RESET_ALL + "\n"


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
print("lib[x]264 - CPU Encoding")
print("h264_[n]venc - NVIDIA GPU Encoding")
print("h264_[a]mf - AMD GPU Encoding")
print("[O]ther", end="\n\n")

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
print("New Bitrate: " + newBitrate)
print("New FPS: " + newFPS)
print("New Resolution: " + newRes[0] + "x" + newRes[1])
print("Output File: " + outputFile)
print("Codec: " + codec)
confirmConvert = input("Start conversion? (Y/n): ")
if confirmConvert.lower() == "n": sys.exit()
print("Starting conversion...")
with open("temp.txt", "w") as f:
    f.write(f"ffmpeg -i \"{inputFile}\" -c:v {codec} -s {newRes[0]}x{newRes[1]} -b:v {newBitrate}k -bufsize {newBitrate}k -r {newFPS} \"{outputFile}\"\n{outputFile}")