#!/usr/bin/env python3
"""
Sample Data Extractor
Extracts sample entries with metadata from TikTok JSON data and creates a CSV file
"""

import json
import csv
import sys
import os
from datetime import datetime


def extract_samples_to_csv(json_file_path, output_file_path, num_samples=10):
    """
    Extract sample data with metadata to CSV
    
    Args:
        json_file_path (str): Path to the JSON file
        output_file_path (str): Path for the output CSV file
        num_samples (int): Number of samples to extract
    
    Returns:
        dict: Summary information about the extraction
    """
    
    # Read JSON data
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None
    
    # Extract metadata and videos
    metadata = data.get('metadata', {})
    videos = data.get('videos', [])
    
    if not videos:
        print("No videos found in the data")
        return None
    
    # Prepare sample data
    samples = []
    sample_count = 0
    
    for video in videos:
        if sample_count >= num_samples and num_samples != float('inf'):
            break
            
        video_id = video.get('video_id', '')
        original_url = video.get('original_url', '')
        description = video.get('description', '')
        video_url = video.get('video_url', '')
        tags = '|'.join(video.get('tags', [])) if video.get('tags') else ''
        comments = video.get('comments', [])
        total_comments = len(comments)
        
        # Get first comment as sample if available
        sample_comment_username = ''
        sample_comment_nickname = ''
        sample_comment_text = ''
        sample_comment_date = ''
        sample_comment_likes = 0
        sample_comment_replies = 0
        
        if comments:
            first_comment = comments[0]
            sample_comment_username = first_comment.get('_username', '')
            sample_comment_nickname = first_comment.get('_nickname', '')
            sample_comment_text = first_comment.get('_comment', '')
            sample_comment_date = first_comment.get('_create_time', '')
            sample_comment_likes = first_comment.get('_like_count', 0)
            sample_comment_replies = first_comment.get('_total_reply', 0)
        
        # Create sample row
        sample_row = {
            'sample_id': sample_count + 1,
            'video_id': video_id,
            'original_url': original_url,
            'description': description[:100] + '...' if len(description) > 100 else description,  # Truncate long descriptions
            'video_url': video_url,
            'tags': tags,
            'total_comments': total_comments,
            'sample_comment_username': sample_comment_username,
            'sample_comment_nickname': sample_comment_nickname,
            'sample_comment_text': sample_comment_text[:200] + '...' if len(sample_comment_text) > 200 else sample_comment_text,  # Truncate long comments
            'sample_comment_date': sample_comment_date,
            'sample_comment_likes': sample_comment_likes,
            'sample_comment_replies': sample_comment_replies
        }
        
        samples.append(sample_row)
        sample_count += 1
    
    # Write to CSV
    if samples:
        fieldnames = [
            'sample_id', 'video_id', 'original_url', 'description', 'video_url', 'tags', 
            'total_comments', 'sample_comment_username', 'sample_comment_nickname', 
            'sample_comment_text', 'sample_comment_date', 'sample_comment_likes', 'sample_comment_replies'
        ]
        
        with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(samples)
        
        # Summary information
        summary = {
            'total_videos_in_dataset': metadata.get('total_videos', len(videos)),
            'total_comments_in_dataset': metadata.get('total_comments', 0),
            'samples_extracted': len(samples),
            'extraction_date': metadata.get('extraction_date', ''),
            'source': metadata.get('source', ''),
            'output_file': output_file_path,
            'sample_creation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return summary
    
    return None


def main():
    """Main execution function with command line arguments"""
    
    if len(sys.argv) < 2:
        print("🔍 TikTok Data Sample Extractor")
        print("=" * 60)
        print("Usage: python extract_samples.py <json_file> [num_samples] [output_file]")
        print("\nArguments:")
        print("  json_file     Path to the JSON data file (required)")
        print("  num_samples   Number of samples to extract (default: 10, use 'all' for complete conversion)")
        print("  output_file   Output CSV file path (optional, auto-generated if not provided)")
        print("\nExamples:")
        print("  python extract_samples.py lancome_Malaysia_data.json")
        print("  python extract_samples.py lancome_Malaysia_data.json 25")
        print("  python extract_samples.py lancome_Malaysia_data.json all")
        print("  python extract_samples.py data.json 50 my_samples.csv")
        print("\n🌟 Features:")
        print("  • Extract specific number of samples or convert entire dataset")
        print("  • Auto-generates output filename based on input")
        print("  • Handles video metadata and sample comments")
        print("  • Comprehensive extraction statistics")
        return
    
    # Parse arguments
    json_file = sys.argv[1]
    
    # Handle num_samples argument
    if len(sys.argv) > 2:
        if sys.argv[2].lower() == 'all':
            num_samples = None  # Extract all
        else:
            try:
                num_samples = int(sys.argv[2])
            except ValueError:
                print("❌ Error: num_samples must be a number or 'all'")
                return
    else:
        num_samples = 10  # Default
    
    # Handle output file argument
    if len(sys.argv) > 3:
        output_file = sys.argv[3]
    else:
        # Auto-generate output filename
        base_name = os.path.splitext(os.path.basename(json_file))[0]
        output_dir = os.path.dirname(json_file) if os.path.dirname(json_file) else '.'
        if num_samples is None:
            output_file = os.path.join(output_dir, f"{base_name}_complete.csv")
        else:
            output_file = os.path.join(output_dir, f"{base_name}_samples_{num_samples}.csv")
    
    # Validate input file
    if not os.path.exists(json_file):
        print(f"❌ Error: JSON file not found: {json_file}")
        return
    
    # Display extraction info
    if num_samples is None:
        print(f"🔍 Converting complete dataset from {os.path.basename(json_file)}...")
    else:
        print(f"🔍 Extracting {num_samples} samples from {os.path.basename(json_file)}...")
    print("-" * 60)
    
    # Extract samples (handle 'all' case)
    if num_samples is None:
        # For complete conversion, we'll extract all videos
        summary = extract_samples_to_csv(json_file, output_file, num_samples=float('inf'))
    else:
        summary = extract_samples_to_csv(json_file, output_file, num_samples=num_samples)
    
    if summary:
        print(f"✅ Extraction completed!")
        print(f"📁 Output file: {summary['output_file']}")
        print("-" * 60)
        print("📊 EXTRACTION SUMMARY:")
        print(f"   📹 Total videos in dataset: {summary['total_videos_in_dataset']}")
        print(f"   💬 Total comments in dataset: {summary['total_comments_in_dataset']}")
        print(f"   🔢 Samples extracted: {summary['samples_extracted']}")
        print(f"   📅 Original extraction: {summary['extraction_date']}")
        print(f"   🎯 Source: {summary['source']}")
        print(f"   ⏰ Sample creation: {summary['sample_creation_date']}")
        print("-" * 60)
        print("✨ CSV file created successfully!")
    else:
        print("❌ Extraction failed!")


if __name__ == "__main__":
    main()
