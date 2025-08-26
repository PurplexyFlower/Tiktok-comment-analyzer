@echo off
REM Quick Setup Script for TikTok Comment Scrapper - Windows Version
REM This script automates the installation process

echo 🚀 TikTok Comment Scrapper - Quick Setup
echo ========================================

REM Check Python version
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

python -c "import sys; exit(0 if sys.version_info >= (3, 7) else 1)"
if %errorlevel% neq 0 (
    echo ❌ Error: Python 3.7+ is required
    pause
    exit /b 1
)

echo ✅ Python version check passed

REM Create virtual environment
echo 🔧 Creating virtual environment...
python -m venv .venv

REM Activate virtual environment
echo 🪟 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo 📦 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Verify installation
echo ✅ Verifying installation...
python main.py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Main scraper: OK
) else (
    echo ❌ Main scraper: FAILED
)

python scrape_from_urls.py --help >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Batch scraper: OK
) else (
    echo ❌ Batch scraper: FAILED
)

python tools\flexible_consolidate.py --help >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Consolidation tools: OK
) else (
    echo ❌ Consolidation tools: FAILED
)

echo.
echo 🎉 Setup Complete!
echo.
echo 🚀 Quick Start Commands:
echo   Single video:  python main.py --aweme_id 7488733265222798614
echo   Batch process: python scrape_from_urls.py -f URLs/lancomethailand_urls.txt -o thailand_output
echo   Consolidate:   python tools/flexible_consolidate.py -i thailand_output -o lancome_Thailand
echo.
echo 📚 Documentation:
echo   Full guide:    type USAGE_GUIDE.md
echo   Project info:  type PROJECT_REPORT.md
echo   Tools help:    type tools\README.md
echo.
pause
