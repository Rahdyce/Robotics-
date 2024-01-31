@echo off

REM Check if pip is installed
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not installed. Please install pip before running this script.
    exit /b 1
)

REM Install packages
python -m pip install torch pyaudio pytube

REM Check if installation was successful
if %errorlevel% neq 0 (
    echo Error: Failed to install packages. Please check the error messages above.
) else (
    echo Packages installed successfully.
)