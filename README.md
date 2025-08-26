# 🎯 TikTok Comment Scrapper

[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)](PROJECT_REPORT.md)

![TikTok Scraper Banner](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GA-U-u2bsAApmn9.jpeg)

**Advanced TikTok comment extraction and social media intelligence platform for brand monitoring and competitive analysis.**

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/romysaputrasihananda/tiktok-comment-scrapper
cd tiktok-comment-scrapper

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

## 🚀 Installation

### Standard Installation
```bash
# Clone repository
git clone https://github.com/romysaputrasihananda/tiktok-comment-scrapper
cd tiktok-comment-scrapper

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

```sh
python main.py --url=7170139292767882522 --size=10 --output=data
```

### Flags

| Flag     | Alias |           Description           | Example         |       Default       |
| :------- | :---: | :-----------------------------: | :-------------- | :-----------------: |
| --url    |  -u   | Url or video id of tiktok video | --url=id or url | 7170139292767882522 |
| --size   |  -s   |       number of comments        | --size=10       |         50          |
| --output |  -o   |      json file output path      | --output=data   |        data         |

## Sample Output

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/Screenshot_20231211_001804.png)

```json
{
  "caption": "makk aku jadi animee🤩#faceplay #faceplayapp #anime #harem #xysryo ",
  "date_now": "2023-12-10T22:06:04",
  "video_url": "https://t.tiktok.com/i18n/share/video/7170139292767882522/?_d=0&comment_author_id=6838487455625479169&mid=7157599449395496962&preview_pb=0&region=ID&share_comment_id=7310977412674093829&share_item_id=7170139292767882522&sharer_language=en&source=h5_t&u_code=0",
  "comments": [
    {
      "username": "user760722966",
      "nickname": "rehan",
      "comment": "testing 😁😁",
      "create_time": "2023-12-10T21:46:36",
      "avatar": "https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/f64f2c7df8a16098d3b3c80e958ffc52~c5_100x100.jpg?x-expires=1702306800&x-signature=KhUeuGmPAVij9A8gbgh7wK6rn98%3D",
      "total_reply": 0,
      "replies": []
    },
    {
      "username": "user760722966",
      "nickname": "rehan",
      "comment": "bagus",
      "create_time": "2023-12-10T18:55:47",
      "avatar": "https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/f64f2c7df8a16098d3b3c80e958ffc52~c5_100x100.jpg?x-expires=1702306800&x-signature=KhUeuGmPAVij9A8gbgh7wK6rn98%3D",
      "total_reply": 3,
      "replies": [
        {
          "username": "ryo.syntax",
          "nickname": "Bukan Rio",
          "comment": "good game",
          "create_time": "2023-12-10T18:56:19",
          "avatar": "https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/be4a9d0479f29d00cb3d06905ff5a972~c5_100x100.jpg?x-expires=1702306800&x-signature=IvkeSvXmvkmE0hZG5dtgpqcFn3A%3D"
        }
        // more replies
      ]
    }
    // more comments
  ]
}
```

## License

This project is licensed under the [MIT License](LICENSE).
