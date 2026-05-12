@echo off
chcp 65001 > nul
pushd "%~dp0"
title LegalKit Pro EN v7.47 build (torch excluded, D-drive TEMP)
set TAG=EN

if not exist "_temp" mkdir "_temp"
set "TEMP=%CD%\_temp"
set "TMP=%CD%\_temp"

echo Step 1 of 6 - pip install base dependencies
python -m pip install pyinstaller pyinstaller-hooks-contrib pillow pypdf2 tkinterdnd2 cryptography imageio-ffmpeg numpy faster-whisper ctranslate2 nvidia-cublas-cu12 nvidia-cudnn-cu12 --upgrade --quiet
if errorlevel 1 ( echo ERROR pip failed & popd & pause & exit /b 1 )

echo Step 2 of 6 - copy NVIDIA DLLs to ASCII path with cuDNN whitelist
if not exist "_nv_dlls" (
    echo _nv_dlls 없음 - v711 폴더에서 복사 중...
    xcopy /E /I /Q "..\install_legalkit_v711\_nv_dlls" "_nv_dlls"
)
python "_resolve_nvidia.py"
if errorlevel 1 ( echo ERROR DLL copy failed & popd & pause & exit /b 1 )

echo Step 3 of 6 - PyInstaller onedir EXE build (torch excluded)
python -m PyInstaller --noconfirm --onedir --windowed --name "LegalKit_%TAG%" --distpath "dist_pro" --workpath "build_pro" --specpath "." --hidden-import tkinterdnd2 --collect-all tkinterdnd2 --hidden-import cryptography --collect-submodules cryptography --hidden-import faster_whisper --collect-all faster_whisper --hidden-import ctranslate2 --collect-all ctranslate2 --collect-binaries ctranslate2 --hidden-import imageio_ffmpeg --collect-all imageio_ffmpeg --hidden-import numpy --hidden-import tokenizers --exclude-module torch --exclude-module torchvision --exclude-module torchaudio --exclude-module llvmlite --add-binary "_nv_dlls/cublas/*.dll;." --add-binary "_nv_dlls/cudnn/*.dll;." "LegalKit_%TAG%_v747.py"
if errorlevel 1 ( echo ERROR PyInstaller failed & popd & pause & exit /b 1 )

echo Step 4 of 6 - locate Inno Setup compiler
set "ISCC=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" ( echo ERROR Inno Setup not found & popd & pause & exit /b 1 )

echo Step 5 of 6 - Inno Setup compile
"%ISCC%" "LegalKit_Pro_%TAG%.iss"
if errorlevel 1 ( echo ERROR Inno Setup failed & popd & pause & exit /b 1 )

echo Step 6 of 6 - DONE %CD%\installer_out\LegalKit_Pro_EN_v7.47_setup.exe
popd
pause
