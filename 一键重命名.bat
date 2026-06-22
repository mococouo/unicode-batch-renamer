@echo off
chcp 65001 >nul
echo ========================================
echo   Unicode Batch Renamer
echo ========================================
echo.
echo Starting the graphical interface...
echo.

python batch_rename_gui.py

if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo Error: unable to start the program
    echo ========================================
    echo.
    echo Please make sure Python 3 is installed.
    echo You can also run: python rename_images_simple.py
    echo.
    pause
)
