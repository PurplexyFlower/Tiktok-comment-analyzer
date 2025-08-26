# 🛠️ Tools Directory

This directory contains utility scripts for processing and organizing TikTok data. Each tool serves a specific purpose in the data extraction and organization workflow.

## 📁 File Overview

### 📊 Data Consolidation Tools

#### `consolidate_json.py`
**Purpose**: Combines multiple individual JSON files into one comprehensive JSON file  
**Usage**: Merges all video comment JSON files from `LancomeVideos_comments/` into a single structured file  
**Output**: `all_videos_comments.json` with metadata and complete comment data  
**Features**:
- Processes comment objects and replies
- Adds metadata (total videos, comments, extraction date)
- Preserves data structure and relationships

#### `consolidate_text.py`
**Purpose**: Combines multiple individual text files into one readable text file  
**Usage**: Merges all video comment text files from `LancomeVideos_comments/` into a single formatted file  
**Output**: `all_videos_comments.txt` with clear separators and organization  
**Features**:
- Adds video separators and numbering
- Includes generation timestamps
- Creates readable format for human consumption

### 🔗 URL Processing Tools

#### `extract_urls_from_json.py`
**Purpose**: Extracts video URLs from the LancomeVideos.json file  
**Usage**: Reads the main JSON file and extracts all video URLs to `sample_urls.txt`  
**Output**: Appends URLs to sample_urls.txt for scraping workflows  
**Features**:
- Validates URL existence before extraction
- Appends to existing files without overwriting
- Provides extraction statistics

#### `convert_urls_to_json.py`
**Purpose**: Converts URL text files to structured JSON format  
**Usage**: Transforms `urls_products_by_tags.txt` into organized JSON with metadata  
**Output**: `urls_products_by_tags.json` with structured URL data  
**Features**:
- Adds comprehensive metadata
- Counts and validates URLs
- Creates ISO timestamp for tracking

### 📝 Data Formatting Tools

#### `sample_extractor.py`
**Purpose**: Extracts sample data with metadata from TikTok JSON files to CSV format  
**Usage**: `python sample_extractor.py <json_file> [num_samples] [output_file]`  
**Arguments**:
- `json_file` - Path to the JSON data file (required)
- `num_samples` - Number of samples to extract (default: 10, use 'all' for complete conversion)
- `output_file` - Output CSV file path (optional, auto-generated if not provided)
**Examples**:
- `python sample_extractor.py lancome_Malaysia_data.json` (extract 10 samples)
- `python sample_extractor.py lancome_Malaysia_data.json 25` (extract 25 samples)
- `python sample_extractor.py lancome_Malaysia_data.json all` (convert entire dataset)
- `python sample_extractor.py data.json 50 my_samples.csv` (custom output file)
**Features**:
- Flexible sample size selection or complete dataset conversion
- Auto-generates meaningful output filenames
- Extracts video metadata and sample comments
- Comprehensive extraction statistics and summaries
- UTF-8 encoding support for international content

#### `format_to_text.py`
**Purpose**: Converts individual JSON comment files to human-readable text format  
**Usage**: `python format_to_text.py --json-file input.json --output-file output.txt`  
**Output**: Formatted text files with comments, replies, and user information  
**Features**:
- Command-line interface with Click
- Formats comments with proper indentation
- Includes user metadata (username, nickname, avatar)
- Processes nested replies with clear hierarchy

#### `organize_results.py`
**Purpose**: Organizes and structures scraping results into proper directories  
**Usage**: Automatically called after scraping operations to clean up output  
**Output**: Organized directory structure with categorized results  
**Features**:
- Creates proper folder hierarchies
- Moves files to appropriate locations
- Generates summary reports

## 🚀 Usage Examples

### Consolidating All Comments
```bash
# Consolidate JSON files
python tools/consolidate_json.py

# Consolidate text files  
python tools/consolidate_text.py
```

### URL Processing
```bash
# Extract URLs from main JSON
python tools/extract_urls_from_json.py

# Convert URL text to JSON
python tools/convert_urls_to_json.py
```

### Individual File Formatting
```bash
# Convert single JSON to text
python tools/format_to_text.py --json-file video_123.json --output-file video_123.txt
```

## 📋 Requirements

- Python 3.7+
- Required packages: `json`, `click`, `datetime`, `os`
- Input files should be in the parent directory
- Proper directory structure for LancomeVideos_comments/

## 🔄 Workflow Integration

1. **Data Extraction**: Use main scraping scripts to collect TikTok data
2. **Individual Processing**: Use `format_to_text.py` for single file conversions
3. **Organization**: Use `organize_results.py` to structure output
4. **Consolidation**: Use consolidation tools to merge all results
5. **URL Management**: Use URL tools to prepare new scraping targets

## 📊 Output Structure

```
LancomeVideos_comments/
├── individual_files.json       # Original extracted files
├── individual_files.txt        # Formatted versions
├── all_videos_comments.json    # Consolidated JSON (consolidate_json.py)
├── all_videos_comments.txt     # Consolidated text (consolidate_text.py)
└── scraping_summary.json       # Metadata and statistics
```

## 🛡️ Error Handling

All tools include:
- File existence validation
- Encoding error handling (UTF-8)
- Progress reporting and statistics
- Graceful failure with informative messages

## 📝 Notes

- Tools are designed to work from the main project directory
- UTF-8 encoding is used throughout for international character support
- JSON files preserve exact data structure from original extractions
- Text files prioritize human readability with clear formatting
