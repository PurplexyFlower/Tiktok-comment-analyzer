#!/usr/bin/env python3
"""
JSON to CSV Converter for TikTok Data
Converts TikTok JSON data files to CSV format with flexible structure handling
"""

import json
import csv
import sys
import os
from datetime import datetime
from pathlib import Path


def convert_json_to_csv(json_file_path, output_dir=None):
    """
    Convert JSON TikTok data to CSV format
    
    Args:
        json_file_path (str): Path to the JSON file
        output_dir (str): Output directory for CSV files (optional)
    
    Returns:
        tuple: (videos_csv_path, comments_csv_path, summary_info)
    """
    
    # Read JSON data
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None, None, None
    
    # Set up output directory and file names
    if output_dir is None:
        output_dir = os.path.dirname(json_file_path)
    
    base_name = Path(json_file_path).stem
    videos_csv_path = os.path.join(output_dir, f"{base_name}_videos.csv")
    comments_csv_path = os.path.join(output_dir, f"{base_name}_comments.csv")
    summary_csv_path = os.path.join(output_dir, f"{base_name}_summary.csv")
    
    # Extract metadata
    metadata = data.get('metadata', {})
    videos = data.get('videos', [])
    
    # Prepare video data for CSV
    video_rows = []
    comment_rows = []
    
    for video in videos:
        # Handle video-level data
        video_row = {
            'video_id': video.get('video_id', ''),
            'original_url': video.get('original_url', ''),
            'description': video.get('description', ''),
            'video_url': video.get('video_url', ''),
            'tags': '|'.join(video.get('tags', [])) if video.get('tags') else '',
            'total_comments': video.get('total_comments', 0)
        }
        video_rows.append(video_row)
        
        # Handle comments if they exist
        comments = video.get('comments', [])
        for comment in comments:
            comment_row = {
                'video_id': video.get('video_id', ''),
                'comment_id': comment.get('id', ''),
                'author_username': comment.get('author', {}).get('username', '') if isinstance(comment.get('author'), dict) else comment.get('author', ''),
                'author_nickname': comment.get('author', {}).get('nickname', '') if isinstance(comment.get('author'), dict) else '',
                'content': comment.get('content', ''),
                'like_count': comment.get('like_count', 0),
                'reply_count': comment.get('reply_count', 0),
                'timestamp': comment.get('timestamp', ''),
                'create_time': comment.get('create_time', ''),
                'is_liked': comment.get('is_liked', False)
            }
            comment_rows.append(comment_row)
    
    # Write videos CSV
    if video_rows:
        video_fieldnames = ['video_id', 'original_url', 'description', 'video_url', 'tags', 'total_comments']
        with open(videos_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=video_fieldnames)
            writer.writeheader()
            writer.writerows(video_rows)
        
        print(f"✅ Videos CSV created: {videos_csv_path}")
        print(f"   📊 {len(video_rows)} videos exported")
    
    # Write comments CSV (if there are comments)
    if comment_rows:
        comment_fieldnames = ['video_id', 'comment_id', 'author_username', 'author_nickname', 
                             'content', 'like_count', 'reply_count', 'timestamp', 'create_time', 'is_liked']
        with open(comments_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=comment_fieldnames)
            writer.writeheader()
            writer.writerows(comment_rows)
        
        print(f"✅ Comments CSV created: {comments_csv_path}")
        print(f"   💬 {len(comment_rows)} comments exported")
    else:
        comments_csv_path = None
        print("ℹ️  No comments found in the data - comments CSV not created")
    
    # Write summary CSV
    summary_data = [
        ['Metric', 'Value'],
        ['Total Videos', metadata.get('total_videos', len(video_rows))],
        ['Total Comments', metadata.get('total_comments', len(comment_rows))],
        ['Extraction Date', metadata.get('extraction_date', '')],
        ['Source', metadata.get('source', 'TikTok')],
        ['Input Directory', metadata.get('input_directory', '')],
        ['Output Directory', metadata.get('output_directory', '')],
        ['Videos with Comments', sum(1 for v in video_rows if v['total_comments'] > 0)],
        ['Videos without Comments', sum(1 for v in video_rows if v['total_comments'] == 0)],
        ['Average Comments per Video', round(len(comment_rows) / len(video_rows), 2) if video_rows else 0],
        ['Conversion Date', datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    ]
    
    with open(summary_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(summary_data)
    
    print(f"✅ Summary CSV created: {summary_csv_path}")
    
    # Summary information
    summary_info = {
        'total_videos': len(video_rows),
        'total_comments': len(comment_rows),
        'videos_with_comments': sum(1 for v in video_rows if v['total_comments'] > 0),
        'videos_without_comments': sum(1 for v in video_rows if v['total_comments'] == 0)
    }
    
    return videos_csv_path, comments_csv_path, summary_info


def main():
    """Main function to handle command line execution"""
    
    if len(sys.argv) < 2:
        print("Usage: python json_to_csv_converter.py <json_file_path> [output_directory]")
        print("\nExample:")
        print("  python json_to_csv_converter.py lancome_Malaysia_data.json")
        print("  python json_to_csv_converter.py lancome_Malaysia_data.json ./csv_output/")
        return
    
    json_file_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(json_file_path):
        print(f"Error: JSON file not found: {json_file_path}")
        return
    
    print(f"🔄 Converting {json_file_path} to CSV format...")
    print("-" * 60)
    
    videos_csv, comments_csv, summary = convert_json_to_csv(json_file_path, output_dir)
    
    if summary:
        print("-" * 60)
        print("📊 CONVERSION SUMMARY:")
        print(f"   📹 Total Videos: {summary['total_videos']}")
        print(f"   💬 Total Comments: {summary['total_comments']}")
        print(f"   ✅ Videos with Comments: {summary['videos_with_comments']}")
        print(f"   ❌ Videos without Comments: {summary['videos_without_comments']}")
        print("-" * 60)
        print("✨ Conversion completed successfully!")
    else:
        print("❌ Conversion failed!")


if __name__ == "__main__":
    main()
