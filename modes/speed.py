import os
import sys
import colorama as color
from videoprops import get_audio_properties
color.init()
path = os.getenv('PATH').split(';')
end = color.Style.RESET_ALL + "\n"

rmAudio = False

inputFile = input("Input file: ")
speed = input("Video Speed: ")
newFPS = input("New FPS: ")
confirmConvert = input("Remove Audio? (y/N): ")
if confirmConvert.lower() == "y": rmAudio = True
audioInfo = get_audio_properties(inputFile)
sampleRate = audioInfo['sample_rate']
sampleConfirm = input("Detected Sample Rate: " + sampleRate + "\nIs this correct? (Y/n): ")
if sampleConfirm.lower() == "n": sampleRate = input("Audio Sample Rate: ")
outputFile = input("Output file: ")
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
print("Sample Rate: " + sampleRate)
print("Video Speed: " + speed)
print("New FPS: " + newFPS)
print("Output File: " + outputFile)
print("Codec: " + codec)
confirmConvert = input("Start conversion? (Y/n): ")
if confirmConvert.lower() == "n": sys.exit()
print("Starting conversion...")
with open("temp.txt", "w") as f:
    f.write(f"ffmpeg -i \"{inputFile}\" -c:v {codec} -filter_complex \"[0:v]setpts=PTS/{speed}[v];[0:a]asetrate={sampleRate}*{speed}[a]\" -map \"[v]\" -map \"[a]\" -r {newFPS} \"{outputFile}\"\n{outputFile}")