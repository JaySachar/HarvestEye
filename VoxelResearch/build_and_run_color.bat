@echo off
REM Compile the C++ code
g++ color_to_voxel.cpp -o color_to_voxel.exe

REM Check if compilation was successful
IF %ERRORLEVEL% NEQ 0 (
    echo Compilation failed.
    exit /b 1
)

REM Run the compiled executable
color_to_voxel.exe
