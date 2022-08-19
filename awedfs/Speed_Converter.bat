@echo off
title MotdHS's Video Speed converter
:n
cls
set /p "file=Input file name: "
set /p "speed=New speed: "
set /p "fps=New FPS: "
set /p "output=Output file name: "
echo.
echo.
echo Input file: %file%.mp4
echo Speed: %speed%X speed
echo FPS: %fps% FPS
echo Output file: %output%.mp4

echo.
echo Is this correct?
set /p "confirm=(y/n): "
goto %confirm%

:y
echo Processing...
echo The video will be converted 2 times.
title MotdHS's Video Speed converter Step 1. Change the sample rate of the video
ffmpeg -i "%file%.mp4" -ar 48000 -ab 256k "%output%_temp.mp4"
title MotdHS's Video Speed converter Step 2. Change the speed of the video
ffmpeg -i "%output%_temp.mp4" -filter_complex "[0:v]setpts=PTS/%speed%[v];[0:a]asetrate=48000*%speed%[a]" -map "[v]" -map "[a]" -r %fps% "%output%.mp4"
echo Deleting temporary file...
del "%output%_temp.mp4"
title MotdHS's Video Speed converter
pause