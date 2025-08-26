#!/bin/bash
# Quick Setup Script for TikTok Comment Scrapper
# This script automates the installation process

echo "🚀 TikTok Comment Scrapper - Quick Setup"
echo "========================================"

# Check Python version
python_version=$(python --version 2>&1 | grep -Po "(?<=Python )\d+\.\d+")
echo "📋 Detected Python version: $python_version"

if ! python -c "import sys; exit(0 if sys.version_info >= (3, 7) else 1)"; then
    echo "❌ Error: Python 3.7+ is required"
    exit 1
fi

# Create virtual environment
echo "🔧 Creating virtual environment..."
python -m venv .venv

# Activate virtual environment (platform specific)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "🪟 Detected Windows - activating environment..."
    source .venv/Scripts/activate
else
    echo "🐧 Detected Unix-like system - activating environment..."
    source .venv/bin/activate
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
echo "✅ Verifying installation..."
if python main.py --version > /dev/null 2>&1; then
    echo "✅ Main scraper: OK"
else
    echo "❌ Main scraper: FAILED"
fi

if python scrape_from_urls.py --help > /dev/null 2>&1; then
    echo "✅ Batch scraper: OK"
else
    echo "❌ Batch scraper: FAILED"
fi

if python tools/flexible_consolidate.py --help > /dev/null 2>&1; then
    echo "✅ Consolidation tools: OK"
else
    echo "❌ Consolidation tools: FAILED"
fi

echo ""
echo "🎉 Setup Complete!"
echo ""
echo "🚀 Quick Start Commands:"
echo "  Single video:  python main.py --aweme_id 7488733265222798614"
echo "  Batch process: python scrape_from_urls.py -f URLs/lancomethailand_urls.txt -o thailand_output"
echo "  Consolidate:   python tools/flexible_consolidate.py -i thailand_output -o lancome_Thailand"
echo ""
echo "📚 Documentation:"
echo "  Full guide:    cat USAGE_GUIDE.md"
echo "  Project info:  cat PROJECT_REPORT.md"
echo "  Tools help:    cat tools/README.md"
echo ""
