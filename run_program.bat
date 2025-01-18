:: ---------------------------------------------------
:: ------Created  : 09/01/2025 - Jesus Reynoso Bourdier
:: ------Modified : 04/02/2025
:: ------Description : Batch program to execute the (Process_Info.py) file.
:: ----------------------------------------------------

@echo off
:: Batch file to run Python script

echo Checking for Python installation...
py --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

:: Navigate to the directory of the .bat file
cd /d "%~dp0"

echo Running Python script...
py "Process_Info.py"
IF ERRORLEVEL 1 (
    echo An error occurred while running the script.
    pause
) ELSE (
    echo Script executed successfully.
    pause
)