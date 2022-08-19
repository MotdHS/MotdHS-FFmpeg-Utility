@echo off
title MotdHS's MP4 Quality converter
:n
cls
set /p "file=Input file name: "
set /p "bitrate=New bitrate (in kbps): "
set /p "resolution=New resolution: "
set /p "fps=New FPS: "
set /p "output=Output file name: "
echo.
echo.
echo Input file: %file%.mp4
echo Bitrate: %bitrate% kbps
echo Resolution: %resolution%
echo FPS: %fps% FPS
echo Output file: %output%.mp4

echo.
echo Is this correct?
set /p "confirm=(y/n): "
goto %confirm%

:y
echo Processing...
ffmpeg -i "%file%.mp4" -s %resolution% -b:v %bitrate%k -bufsize %bitrate%k -r %fps% "%output%.mp4"
pause