# 🎯 TikTok Comment Analyzer - Enhanced Edition


**Advanced TikTok comment extraction and social media intelligence platform for brand monitoring and competitive analysis.**

## 📋 Credits & Enhancements

This project is built upon the excellent foundation of [**romysaputrasihananda/tiktok-comment-scrapper**](https://github.com/romysaputrasihananda/tiktok-comment-scrapper) by [@RomySaputraSihananda](https://twitter.com/RomySihananda).

### 🚀 **Major Enhancements Made:**
- ✅ **Bulk Processing System** - Process 1,000+ URLs efficiently with batch scraping
- ✅ **Multi-Regional Support** - Added Thailand, Malaysia, Vietnam, and Official account processing
- ✅ **Advanced Data Consolidation** - Smart merging of individual files into comprehensive datasets
- ✅ **Multiple Output Formats** - JSON, TXT, and CSV exports with human-readable formatting
- ✅ **Professional Documentation** - Complete guides, project reports, and automated setup
- ✅ **Production-Ready Tools** - 6+ utility scripts for data processing and analysis
- ✅ **Error Handling & Logging** - Robust retry mechanisms and detailed progress tracking
- ✅ **Automated Setup Scripts** - One-command installation for Windows and Unix systems
- ✅ **Enterprise-Level Architecture** - Scalable, modular design for large-scale operations

**Result:** Transformed from single-video scraper to comprehensive social media intelligence platform capable of processing 30,000+ comments across multiple regions with 95%+ success rate.

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/PurplexyFlower/Tiktok-comment-analyzer.git
cd Tiktok-comment-analyzer

# 2. Setup environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start scraping
python scrape_from_urls.py -f "URLs/lancomethailand_urls.txt" -o "thailand_data"
```

## 📊 Project Overview

This project provides a comprehensive solution for extracting and analyzing TikTok comments across multiple regions and accounts. Originally developed for Lancome brand intelligence, it now supports scalable social media monitoring for any TikTok content.

### 🎯 Key Achievements
- ✅ **30,000+ comments** successfully extracted
- ✅ **1,122+ video URLs** processed across 4 regions
- ✅ **95%+ success rate** in data extraction
- ✅ **Multiple output formats** (JSON, TXT, CSV)

## 🛠️ Core Features

### 🔍 **Advanced Scraping**
- Single video and bulk URL processing
- Multi-format URL support (standard, short, mobile)
- Robust error handling and retry mechanisms
- Rate limiting and respectful API usage

### 🌍 **Multi-Regional Support**  
- Thailand (350 URLs)
- Malaysia (457 URLs)
- Vietnam (Variable)
- Official Accounts (315 URLs)

### 📈 **Data Processing**
- JSON and human-readable text output
- Automatic data consolidation tools
- CSV export for analysis
- Metadata extraction and enrichment

### 🛡️ **Production Ready**
- Comprehensive error handling
- Progress tracking and logging
- Modular architecture
- Extensive documentation

## 📋 Requirements

- **Python 3.7+** (Tested on 3.7, 3.8, 3.9, 3.10, 3.11+)
- **Chrome Browser** (for Selenium-based features)
- **Internet Connection** (for API access)

### Core Dependencies
- `requests>=2.31.0` - HTTP client
- `click>=8.0.0` - CLI framework  
- `loguru>=0.7.0` - Advanced logging
- `selenium>=4.15.0` - Web automation


## License

This project is licensed under the [MIT License](LICENSE).
