# MotdHS-FFmpeg-Utility

**NOTE: This project has now been abandoned, and I will start working on a rewrite soon**

A tool written in Python that uses FFmpeg to modify a video/audio file.

<h3>This tool is still work in progress, and there might be some bugs.</h3>

<h3>It's only tested in Windows, so I can't guarantee that it will work on Linux or Mac OS. </h3>

## Features
- Change Bitrate, FPS, Resolution of a video
- Change Speed of a video

## How to build - Windows
- Download and Install python at https://www.python.org/ (Make sure you check "Add Python 3.x to PATH")

- Open Command Prompt, and navigate to the folder.

- Type in `pip install -r requirements.txt`, and `pip install pyinstaller`.

- After that, you can build with `pyinstaller main.py --onefile`.

- The .exe file should be in "dist" folder
