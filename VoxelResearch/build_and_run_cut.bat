@echo off
REM Compile the C++ code
g++ cut_to_voxel.cpp -o cut_to_voxel.exe

REM Check if compilation was successful
IF %ERRORLEVEL% NEQ 0 (
    echo Compilation failed.
    exit /b 1
)

REM Run the compiled executable
cut_to_voxel.exe

