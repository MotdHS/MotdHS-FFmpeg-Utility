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
title MotdHS's Video Speed converter - Converting...
ffmpeg -i "%file%.mp4" -filter_complex "[0:v]setpts=PTS/%speed%[v]" -map "[v]" -r %fps% "%output%.mp4"
title MotdHS's Video Speed converter
pause