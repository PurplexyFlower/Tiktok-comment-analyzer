import click
import json
import os
import re
from tiktokcomment import TiktokComment

def extract_video_id(url):
    """
    Extracts the video ID from a TikTok URL.
    Supports various TikTok URL formats.
    """
    # Common TikTok URL patterns
    patterns = [
        r'tiktok\.com/@[^/]+/video/(\d+)',  # Standard format
        r'tiktok\.com/t/(\w+)',             # Short link format
        r'vm\.tiktok\.com/(\w+)',           # Mobile format
        r'/video/(\d+)',                    # Just the video part
        r'^(\d+)$'                          # Just the ID
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def read_urls_from_file(file_path):
    """
    Reads URLs from a text file, one URL per line.
    Ignores empty lines and lines starting with #.
    """
    urls = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    video_id = extract_video_id(line)
                    if video_id:
                        urls.append((line, video_id))
                    else:
                        print(f"Warning: Could not extract video ID from line {line_num}: {line}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return []
    
    return urls

@click.command(help="Scrape comments from TikTok videos listed in a text file.")
@click.option('--urls-file', '-f', required=True, help='Text file containing TikTok URLs (one per line)')
@click.option('--output-dir', '-o', default='scraped_data', help='Directory to save the output files')
@click.option('--create-sample', '-s', is_flag=True, help='Create a sample URLs file')
def main(urls_file, output_dir, create_sample):
    """
    Scrapes comments from TikTok videos listed in a text file.
    """
    
    # Create sample file if requested
    if create_sample:
        sample_content = """# TikTok URLs to scrape (one per line)
# Lines starting with # are ignored
# Supported formats:
# - Full URLs: https://www.tiktok.com/@username/video/1234567890
# - Short URLs: https://vm.tiktok.com/abc123
# - Video IDs only: 1234567890

# Example URLs (remove # to use):
# https://www.tiktok.com/@lancome.official/video/7488733265222798614
# https://www.tiktok.com/@lancome.official/video/7170139292767882522
"""
        with open('sample_urls.txt', 'w', encoding='utf-8') as f:
            f.write(sample_content)
        print("Created 'sample_urls.txt' - edit this file with your TikTok URLs")
        return
    
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read URLs from file
    url_data = read_urls_from_file(urls_file)
    if not url_data:
        print("No valid URLs found in the file.")
        return
    
    print(f"Found {len(url_data)} valid URLs to process...")
    
    # Initialize scraper
    scraper = TiktokComment()
    all_data = {}
    successful_scrapes = 0
    
    for i, (original_url, video_id) in enumerate(url_data, 1):
        print(f"\n[{i}/{len(url_data)}] Scraping video ID: {video_id}")
        print(f"Original URL: {original_url}")
        
        try:
            # Scrape comments
            comments_data = scraper(aweme_id=video_id)
            
            video_data = {
                "original_url": original_url,
                "video_id": video_id,
                "description": comments_data.caption,
                "video_url": comments_data.video_url,
                "tags": [word for word in (comments_data.caption or "").split() if word.startswith('#')],
                "comments": comments_data.comments,
                "total_comments": len(comments_data.comments)
            }
            
            all_data[video_id] = video_data
            
            # Save individual files for each video
            # JSON file
            with open(os.path.join(output_dir, f"{video_id}.json"), 'w', encoding='utf-8') as f:
                json.dump(video_data, f, ensure_ascii=False, indent=4, default=lambda o: o.__dict__)
            
            # Human-readable text file
            with open(os.path.join(output_dir, f"{video_id}.txt"), 'w', encoding='utf-8') as f:
                f.write(f"Video ID: {video_id}\n")
                f.write(f"Original URL: {original_url}\n")
                f.write(f"Description: {video_data['description']}\n")
                f.write(f"Tags: {' '.join(video_data['tags'])}\n")
                f.write(f"Video URL: {video_data['video_url']}\n")
                f.write(f"Total Comments: {video_data['total_comments']}\n\n")
                f.write("="*70 + "\n")
                f.write("COMMENTS\n")
                f.write("="*70 + "\n\n")
                
                for comment in video_data['comments']:
                    f.write(f"👤 {comment.nickname} (@{comment.username})\n")
                    f.write(f"💬 {comment.comment}\n")
                    f.write(f"📅 {comment.create_time}\n")
                    
                    if comment.replies:
                        f.write(f"    └── {len(comment.replies)} replies:\n")
                        for reply in comment.replies:
                            f.write(f"    👤 {reply.nickname} (@{reply.username})\n")
                            f.write(f"    💬 {reply.comment}\n")
                            f.write(f"    📅 {reply.create_time}\n")
                            f.write("    " + "-"*40 + "\n")
                    
                    f.write("\n" + "-"*70 + "\n\n")
            
            successful_scrapes += 1
            print(f"✅ Successfully scraped {len(comments_data.comments)} comments")
            
        except Exception as e:
            print(f"❌ Failed to scrape video {video_id}: {e}")
            continue
    
    # Save summary file with all data
    summary_file = os.path.join(output_dir, 'scraping_summary.json')
    summary_data = {
        "total_urls": len(url_data),
        "successful_scrapes": successful_scrapes,
        "failed_scrapes": len(url_data) - successful_scrapes,
        "videos": all_data
    }
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, ensure_ascii=False, indent=4, default=lambda o: o.__dict__)
    
    # Create CSV summary
    csv_file = os.path.join(output_dir, 'videos_summary.csv')
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        f.write("Video ID,Original URL,Description,Total Comments,Tags\n")
        for video_id, data in all_data.items():
            description = (data['description'] or '').replace('"', '""')  # Escape quotes
            tags = ' '.join(data['tags'])
            f.write(f'"{video_id}","{data["original_url"]}","{description}","{data["total_comments"]}","{tags}"\n')
    
    print(f"\n🎉 Scraping complete!")
    print(f"📊 Results: {successful_scrapes}/{len(url_data)} videos successfully scraped")
    print(f"📁 Data saved in '{output_dir}' directory:")
    print(f"   - Individual JSON files: {video_id}.json")
    print(f"   - Individual text files: {video_id}.txt")
    print(f"   - Summary JSON: scraping_summary.json")
    print(f"   - CSV summary: videos_summary.csv")

if __name__ == '__main__':
    main()
