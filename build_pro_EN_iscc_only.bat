@echo off
chcp 65001 > nul
pushd "%~dp0"
title LegalKit Pro EN - ISCC only with D-drive TEMP

if not exist "_temp" mkdir "_temp"
set "TEMP=%CD%\_temp"
set "TMP=%CD%\_temp"
echo TEMP redirected to: %TEMP%

set "ISCC=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" ( echo ERROR Inno Setup not found & popd & pause & exit /b 1 )
if not exist "dist_pro\LegalKit_EN" ( echo ERROR PyInstaller dist_pro\LegalKit_EN folder missing & popd & pause & exit /b 1 )

echo Inno Setup compile (lzma2/normal, D-drive temp)...
"%ISCC%" "LegalKit_Pro_EN.iss"
if errorlevel 1 ( echo ERROR Inno Setup failed & popd & pause & exit /b 1 )

echo DONE Installer at: %CD%\installer_out\LegalKit_Pro_EN_v7.47_setup.exe
popd
pause
