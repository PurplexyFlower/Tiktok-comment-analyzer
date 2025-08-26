# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python main.py --version
```

### Development Installation
```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
python -m pytest tests/

# Format code
black .
```

## 📖 Usage Examples

### Single Video Extraction
```bash
# Extract comments from single video
python main.py --aweme_id 7488733265222798614

# Using full URL
python main.py --aweme_id "https://www.tiktok.com/@lancome.official/video/7488733265222798614"
```

### Bulk Processing
```bash
# Process Thailand Lancome videos
python scrape_from_urls.py -f "URLs/lancomethailand_urls.txt" -o "thailand_output"

# Process Malaysia Lancome videos  
python scrape_from_urls.py -f "URLs/Lancomemalaysia_urls.txt" -o "malaysia_output"

# Custom processing
python scrape_from_urls.py -f your_urls.txt -o custom_output
```

### Data Consolidation
```bash
# Consolidate scraped data into single files
python tools/flexible_consolidate.py -i "thailand_output" -o "lancome_Thailand" -s "TikTok @lancomethailand"

# JSON only consolidation
python tools/flexible_consolidate.py -i "thailand_output" -o "results" --json-only

# Text only consolidation  
python tools/flexible_consolidate.py -i "thailand_output" -o "results" --text-only
```

## 📁 Project Structure

```
tiktok-comment-scrapper/
├── 📄 main.py                     # Single video scraper
├── 📄 scrape_from_urls.py         # Bulk URL processor  
├── 📄 requirements.txt            # Dependencies
├── 📂 tiktokcomment/              # Core scraping library
├── 📂 tools/                      # Utility scripts
│   ├── consolidate_json.py        # JSON consolidation
│   ├── consolidate_text.py        # Text consolidation
│   ├── flexible_consolidate.py    # Universal consolidator
│   └── README.md                  # Tools documentation
├── 📂 URLs/                       # Input URL collections
│   ├── lancomethailand_urls.txt   # 350 Thailand URLs
│   ├── Lancomemalaysia_urls.txt   # 457 Malaysia URLs  
│   └── Lancom_Officila_Urls.txt   # 315 Official URLs
└── 📂 Output directories/         # Regional results
    ├── lancome_Thailand/          # Thailand consolidated data
    ├── lancome_Malaysia/          # Malaysia consolidated data  
    └── Lancome_official/          # Official consolidated data
```

## 📊 Output Formats

### JSON Structure
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
      "original_url": "https://www.tiktok.com/@lancomethailand/video/...",
      "description": "Product launch video...",
      "total_comments": 15,
      "comments": [
        {
          "username": "user123",
          "nickname": "Beauty Lover",
          "comment": "Amazing product! Love it! 💕",
          "create_time": "2025-08-26 10:15:30",
          "replies": []
        }
      ]
    }
  ]
}
```

### Available Outputs
- **JSON**: Structured data for analysis (`all_videos_comments.json`)
- **TXT**: Human-readable format (`all_videos_comments.txt`)
- **CSV**: Spreadsheet compatible (`videos_summary.csv`)
- **Individual Files**: Per-video JSON and TXT files

## 🛠️ Available Tools

### Core Scripts
- `main.py` - Single video comment extraction
- `scrape_from_urls.py` - Bulk URL processing with progress tracking

### Utility Tools (tools/ directory)
- `flexible_consolidate.py` - Universal data consolidation  
- `consolidate_json.py` - JSON file merging
- `consolidate_text.py` - Text file combining
- `format_to_text.py` - Individual file formatting
- `extract_urls_from_json.py` - URL extraction utilities

### Command-Line Options
```bash
# Get help for any script
python script_name.py --help

# Main scraper options
python main.py --aweme_id VIDEO_ID --output OUTPUT_DIR

# Batch scraper options  
python scrape_from_urls.py -f URLS_FILE -o OUTPUT_DIR

# Consolidation options
python tools/flexible_consolidate.py -i INPUT_DIR -o OUTPUT_DIR -s "SOURCE_NAME"
```

## 🚨 Troubleshooting

### Common Issues

**1. Module Not Found Errors**
```bash
# Ensure virtual environment is activated
.venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

**2. Rate Limiting**
```bash
# Use smaller batch sizes
# Add delays between requests
# Monitor for 429 HTTP status codes
```

**3. Chrome/Selenium Issues**
```bash
# Update Chrome browser
# Reinstall selenium dependencies
pip install --upgrade selenium undetected-chromedriver
```

## 📈 Performance Statistics

- **Processing Speed**: 50-100 videos per hour (rate-limited)
- **Success Rate**: 95%+ successful extractions
- **Data Volume**: 30,000+ comments extracted
- **Regional Coverage**: 4 major markets
- **Total URLs Processed**: 1,122+ video URLs

## 📚 Documentation

- **[📋 PROJECT_REPORT.md](PROJECT_REPORT.md)** - Comprehensive project overview
- **[🚀 USAGE_GUIDE.md](USAGE_GUIDE.md)** - Detailed usage instructions  
- **[🛠️ tools/README.md](tools/README.md)** - Utility tools documentation

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Romy Saputra Sihananda**
- Twitter: [@RomySihananda](https://twitter.com/RomySihananda)
- GitHub: [@RomySaputraSihananda](https://github.com/RomySaputraSihananda)

## 🙏 Acknowledgments

- TikTok platform for providing public API access
- Python community for excellent libraries
- Lancome brand for use case inspiration
- Contributors and testers

---

**⭐ Star this repository if it helped you!**

**Last Updated**: August 26, 2025 | **Version**: 2.0.0
