@echo off
title MotdHS's Video Speed converter
:n
cls
set /p "file=Input file name: "
set /p "speed=New speed: "
set /p "fps=New FPS: "
set /p "sample=Audio samplerate in the video (in Hz): "
set /p "output=Output file name: "
echo.
echo.
echo Input file: %file%.mp4
echo Speed: %speed%X speed
echo FPS: %fps% FPS
echo Audio Sample rate in the video: %sample%
echo Output file: %output%.mp4

echo.
echo Is this correct?
set /p "confirm=(y/n): "
goto %confirm%

:y
echo Processing...
title MotdHS's Video Speed converter - Converting...
ffmpeg -i "%file%.mp4" -filter_complex "[0:v]setpts=PTS/%speed%[v];[0:a]asetrate=%sample%*%speed%[a]" -map "[v]" -map "[a]" -r %fps% "%output%.mp4"
title MotdHS's Video Speed converter
pause