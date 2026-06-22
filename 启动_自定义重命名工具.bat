@echo off
chcp 65001 >nul
echo ================================================
echo   Unicode Batch Renamer
echo ================================================
echo   Examples:
echo   {n}        - 1.jpg, 2.png, 3.mp4
echo   photo_     - photo_1.jpg, photo_2.jpg
echo   trip_{n}_  - trip_1_.jpg, trip_2_.jpg
echo ================================================
echo.
echo Starting the graphical interface...
echo.

python batch_rename_gui.py

if %errorlevel% neq 0 (
    echo.
    echo ================================================
    echo Error: unable to start the program
    echo ================================================
    echo.
    echo Please make sure Python 3 is installed.
    echo.
    pause
)
