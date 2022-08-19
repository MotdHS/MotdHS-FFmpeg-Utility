@echo off
title MotdHS's AVI Quality converter
:n
cls
set /p "file=Input file name (avi): "
set /p "bitrate=New bitrate (in kbps): "
set /p "resolution=New resolution: "
set /p "fps=New FPS: "
set /p "output=Output file name (mp4): "
echo.
echo.
echo Input file: %file%.avi
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
title Step 1. Converting the avi file to temporary mp4 file
ffmpeg -i "%file%.avi" "%output%_temp.mp4"
title Step 2. Changing the quality of the temporary mp4 file
ffmpeg -i "%output%_temp.mp4" -s %resolution% -b:v %bitrate%k -bufsize %bitrate%k -r %fps% "%output%.mp4"
echo.
echo Deleting the temporary mp4 file...
del %output%_temp.mp4
echo Conversion completed!
echo Press any key to exit the program.
pause > nul