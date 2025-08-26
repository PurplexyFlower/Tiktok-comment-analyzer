# 🚀 TikTok Comment Scrapper - Usage Guide

## 📚 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Advanced Features](#advanced-features)
5. [Data Processing](#data-processing)
6. [Troubleshooting](#troubleshooting)
7. [Examples](#examples)

## 🏁 Quick Start

### Prerequisites
- Python 3.7 or higher
- Windows 10/11 (tested) or Linux/macOS
- Chrome browser (for Selenium-based features)
- Internet connection

### 5-Minute Setup
```bash
# 1. Clone the repository
git clone https://github.com/RomySaputraSihananda/tiktok-comment-scrapper.git
cd tiktok-comment-scrapper

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Test installation
python main.py --aweme_id 7488733265222798614
```

## 🔧 Installation

### Step 1: Environment Setup
```bash
# Create project directory
mkdir tiktok-scraper
cd tiktok-scraper

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# Linux/macOS:
source .venv/bin/activate
```

### Step 2: Install Dependencies
```bash
# Install from requirements file
pip install -r requirements.txt

# Or install core dependencies manually
pip install requests>=2.31.0
pip install click>=8.0.0
pip install loguru>=0.7.0
pip install selenium>=4.15.0
```

### Step 3: Verify Installation
```bash
# Test main scraper
python main.py --version

# Test batch scraper
python scrape_from_urls.py --help

# Test consolidation tools
python tools/flexible_consolidate.py --help
```

## 📖 Basic Usage

### Single Video Extraction

#### Using main.py
```bash
# Basic usage - single video
python main.py --aweme_id 7488733265222798614

# Custom output directory
python main.py --aweme_id 7488733265222798614 --output custom_output/

# With full URL (automatic ID extraction)
python main.py --aweme_id "https://www.tiktok.com/@lancome.official/video/7488733265222798614"
```

#### Output Structure
```
data/
└── 7488733265222798614.json    # Extracted comments data
```

### Batch Processing

#### Prepare URL File
Create a text file with TikTok URLs (one per line):
```txt
# sample_urls.txt
https://www.tiktok.com/@lancome.official/video/7488733265222798614
https://www.tiktok.com/@lancome.official/video/7170139292767882522
# Comments starting with # are ignored
7418294751977327878    # Video ID only is also supported
```

#### Run Batch Scraper
```bash
# Basic batch processing
python scrape_from_urls.py -f sample_urls.txt -o scraped_data

# Using existing URL files
python scrape_from_urls.py -f "URLs/lancomethailand_urls.txt" -o "thailand_output"
python scrape_from_urls.py -f "URLs/Lancomemalaysia_urls.txt" -o "malaysia_output"
```

#### Batch Output Structure
```
thailand_output/
├── 7527296826265865479.json    # Individual video JSON
├── 7527296826265865479.txt     # Individual video text
├── 7469248776541097224.json    # Another video JSON
├── 7469248776541097224.txt     # Another video text
├── scraping_summary.json       # Overall summary
└── videos_summary.csv          # CSV export
```

## 🎯 Advanced Features

### URL Format Support
The scraper supports multiple URL formats:

```bash
# Standard format
https://www.tiktok.com/@username/video/1234567890

# Short URLs
https://vm.tiktok.com/ZMd1234567/

# Mobile URLs
https://m.tiktok.com/v/1234567890.html

# Just video ID
1234567890
```

### Custom Processing Options

#### Create Sample URL File
```bash
python scrape_from_urls.py --create-sample
# Creates sample_urls.txt with examples
```

#### Selective Processing
```bash
# Process only specific URLs from a file
head -10 URLs/lancomethailand_urls.txt > small_batch.txt
python scrape_from_urls.py -f small_batch.txt -o test_output
```

## 🔄 Data Processing

### Consolidation Tools

#### Using Flexible Consolidator
```bash
# Consolidate scraped data into single files
python tools/flexible_consolidate.py -i "thailand_output" -o "lancome_Thailand" -s "TikTok @lancomethailand"

# JSON only
python tools/flexible_consolidate.py -i "thailand_output" -o "lancome_Thailand" --json-only

# Text only
python tools/flexible_consolidate.py -i "thailand_output" -o "lancome_Thailand" --text-only
```

#### Direct Function Usage
```python
# In Python script
import sys
sys.path.append('tools')
from flexible_consolidate import consolidate_json_files, consolidate_text_files

# Consolidate files
consolidate_json_files('thailand_output', 'lancome_Thailand', 'TikTok @lancomethailand')
consolidate_text_files('thailand_output', 'lancome_Thailand', 'TikTok @lancomethailand')
```

### Output Analysis

#### JSON Structure
```json
{
  "metadata": {
    "total_videos": 350,
    "total_comments": 5247,
    "extraction_date": "2025-08-26T10:30:00",
    "source": "TikTok @lancomethailand"
  },
  "videos": [
    {
      "video_id": "7527296826265865479",
      "original_url": "https://www.tiktok.com/@lancomethailand/video/7527296826265865479",
      "description": "Video description...",
      "total_comments": 15,
      "comments": [
        {
          "username": "user123",
          "nickname": "User Name",
          "comment": "Great product!",
          "create_time": "2025-08-26 10:15:30",
          "replies": []
        }
      ]
    }
  ]
}
```

## 🛠️ Complete Workflow Examples

### Example 1: Thailand Lancome Analysis

```bash
# Step 1: Scrape Thailand URLs
python scrape_from_urls.py -f "URLs/lancomethailand_urls.txt" -o "thailand_raw"

# Step 2: Consolidate results
python tools/flexible_consolidate.py -i "thailand_raw" -o "lancome_Thailand" -s "TikTok @lancomethailand"

# Step 3: Verify results
ls lancome_Thailand/
# Should show: all_videos_comments.json, all_videos_comments.txt
```

### Example 2: Multi-Region Comparison

```bash
# Process all regions
python scrape_from_urls.py -f "URLs/lancomethailand_urls.txt" -o "raw_thailand"
python scrape_from_urls.py -f "URLs/Lancomemalaysia_urls.txt" -o "raw_malaysia"
python scrape_from_urls.py -f "URLs/Lancom_Officila_Urls.txt" -o "raw_official"

# Consolidate each region
python tools/flexible_consolidate.py -i "raw_thailand" -o "final_thailand" -s "Thailand"
python tools/flexible_consolidate.py -i "raw_malaysia" -o "final_malaysia" -s "Malaysia"  
python tools/flexible_consolidate.py -i "raw_official" -o "final_official" -s "Official"
```

### Example 3: URL Extraction from JSON

```bash
# Extract URLs from JSON files to text format
python tools/extract_urls_from_json.py
# Or using the extraction script you created earlier
python extract_thailand_urls.py
```

## 🚨 Troubleshooting

### Common Issues

#### 1. **"Module not found" errors**
```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# Reinstall dependencies
pip install -r requirements.txt
```

#### 2. **"Video ID not found" warnings**
```bash
# Check URL format in your input file
# Ensure URLs are properly formatted
# Remove any extra spaces or characters
```

#### 3. **Rate limiting / blocking**
```bash
# Reduce processing speed by modifying the scraper
# Add delays between requests
# Use smaller batch sizes
```

#### 4. **Chrome/Selenium issues**
```bash
# Update Chrome browser
# Reinstall selenium and chromedriver
pip uninstall selenium undetected-chromedriver
pip install selenium>=4.15.0 undetected-chromedriver>=3.5.0
```

### Debug Mode

#### Enable Detailed Logging
```python
# Add to your script
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Test Single URL First
```bash
# Test with one URL before batch processing
echo "https://www.tiktok.com/@lancome.official/video/7488733265222798614" > test_url.txt
python scrape_from_urls.py -f test_url.txt -o test_debug
```

## 📊 Performance Tips

### Optimization Strategies

1. **Batch Size Management**
   - Process 50-100 URLs per batch for optimal performance
   - Use smaller batches if experiencing rate limiting

2. **Error Recovery**
   - Check failed URLs in the output logs
   - Retry failed extractions separately

3. **Storage Management**
   - Regular cleanup of temporary files
   - Compress large datasets for storage

### Monitoring Progress

```bash
# Monitor output directory size
du -sh thailand_output/

# Count processed files
ls thailand_output/*.json | wc -l

# Check for errors in logs
grep "ERROR" logs/scraper.log
```

## 📞 Support

### Getting Help

1. **Check Documentation**
   - Review this guide
   - Check tool-specific README files
   - Read error messages carefully

2. **Common Solutions**
   - Restart virtual environment
   - Update dependencies
   - Check network connectivity
   - Verify file permissions

3. **Debug Information**
   - Python version: `python --version`
   - Package versions: `pip list`
   - System information: Platform, OS version

### Best Practices

1. **Always use virtual environments**
2. **Test with small datasets first**
3. **Backup important data regularly**
4. **Monitor for platform changes**
5. **Respect rate limits and terms of service**

---

**Last Updated**: August 26, 2025  
**Version**: 2.0.0  
**Compatibility**: Python 3.7+, Windows/Linux/macOS
