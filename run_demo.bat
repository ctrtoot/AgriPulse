@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================
echo          AGRIPULSE - DEMO GIA LAI
echo ==========================================
set OPEN_BROWSER=1
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 server.py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    python server.py
  ) else (
    echo Khong tim thay Python. Cai Python 3.10+ va chon Add Python to PATH.
    pause
  )
)
pause
