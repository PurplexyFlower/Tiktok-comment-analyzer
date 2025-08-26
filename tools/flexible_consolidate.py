import json
import os
from datetime import datetime
import click

def consolidate_json_files(input_dir, output_dir, source_name="TikTok"):
    """Consolidate all individual JSON files into one comprehensive file"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "all_videos_comments.json")
    
    all_videos_data = {
        "metadata": {
            "total_videos": 0,
            "total_comments": 0,
            "extraction_date": datetime.now().isoformat(),
            "source": source_name,
            "input_directory": input_dir,
            "output_directory": output_dir
        },
        "videos": []
    }
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"❌ Error: Input directory '{input_dir}' does not exist!")
        return None
    
    # Get all JSON files (excluding the summary files)
    json_files = [f for f in os.listdir(input_dir) 
                  if f.endswith('.json') and f not in ['scraping_summary.json', 'all_videos_comments.json']]
    
    if not json_files:
        print(f"❌ No JSON files found in '{input_dir}'")
        return None
    
    json_files.sort()  # Sort for consistent ordering
    
    print(f"🔄 Processing {len(json_files)} JSON files from '{input_dir}'...")
    
    for filename in json_files:
        file_path = os.path.join(input_dir, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                video_data = json.load(f)
            
            # Convert comment objects to dictionaries if needed
            if 'comments' in video_data:
                processed_comments = []
                for comment in video_data['comments']:
                    if hasattr(comment, '__dict__'):
                        comment_dict = comment.__dict__
                    else:
                        comment_dict = comment
                    
                    # Process replies too
                    if 'replies' in comment_dict and comment_dict['replies']:
                        processed_replies = []
                        for reply in comment_dict['replies']:
                            if hasattr(reply, '__dict__'):
                                processed_replies.append(reply.__dict__)
                            else:
                                processed_replies.append(reply)
                        comment_dict['replies'] = processed_replies
                    
                    processed_comments.append(comment_dict)
                
                video_data['comments'] = processed_comments
            
            all_videos_data["videos"].append(video_data)
            all_videos_data["metadata"]["total_comments"] += video_data.get("total_comments", 0)
            
            print(f"✅ Processed {filename} - {video_data.get('total_comments', 0)} comments")
            
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
            continue
    
    all_videos_data["metadata"]["total_videos"] = len(all_videos_data["videos"])
    
    # Save consolidated JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_videos_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 JSON consolidation complete!")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total videos: {all_videos_data['metadata']['total_videos']}")
    print(f"💬 Total comments: {all_videos_data['metadata']['total_comments']}")
    
    return output_file

def consolidate_text_files(input_dir, output_dir, source_name="TikTok"):
    """Consolidate all individual text files into one comprehensive file"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "all_videos_comments.txt")
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"❌ Error: Input directory '{input_dir}' does not exist!")
        return None
    
    # Get all TXT files
    txt_files = [f for f in os.listdir(input_dir) 
                 if f.endswith('.txt') and f != 'all_videos_comments.txt']
    
    if not txt_files:
        print(f"❌ No TXT files found in '{input_dir}'")
        return None
    
    txt_files.sort()  # Sort for consistent ordering
    
    print(f"🔄 Processing {len(txt_files)} text files from '{input_dir}'...")
    
    with open(output_file, 'w', encoding='utf-8') as output_f:
        # Write header
        output_f.write("="*80 + "\n")
        output_f.write(f"{source_name.upper()} VIDEOS - ALL COMMENTS CONSOLIDATED\n")
        output_f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        output_f.write(f"Total Files: {len(txt_files)}\n")
        output_f.write(f"Source: {source_name}\n")
        output_f.write(f"Input Directory: {input_dir}\n")
        output_f.write(f"Output Directory: {output_dir}\n")
        output_f.write("="*80 + "\n\n")
        
        total_videos = 0
        
        for i, filename in enumerate(txt_files, 1):
            file_path = os.path.join(input_dir, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add video separator
                output_f.write(f"\n{'='*80}\n")
                output_f.write(f"VIDEO {i:03d} OF {len(txt_files)}\n")
                output_f.write(f"FILE: {filename}\n")
                output_f.write(f"{'='*80}\n\n")
                
                # Write the content
                output_f.write(content)
                output_f.write(f"\n\n{'='*80}\n")
                output_f.write(f"END OF VIDEO {i:03d}\n")
                output_f.write(f"{'='*80}\n\n")
                
                total_videos += 1
                print(f"✅ Processed {filename}")
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
                continue
        
        # Write footer
        output_f.write(f"\n{'='*80}\n")
        output_f.write(f"CONSOLIDATION COMPLETE\n")
        output_f.write(f"Total Videos Processed: {total_videos}\n")
        output_f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        output_f.write(f"{'='*80}\n")
    
    print(f"\n🎉 Text consolidation complete!")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total videos processed: {total_videos}")
    
    return output_file

@click.command()
@click.option('--input-dir', '-i', required=True, help='Input directory containing individual files')
@click.option('--output-dir', '-o', required=True, help='Output directory for consolidated files')
@click.option('--source-name', '-s', default='TikTok', help='Source name for metadata (default: TikTok)')
@click.option('--json-only', is_flag=True, help='Consolidate only JSON files')
@click.option('--text-only', is_flag=True, help='Consolidate only text files')
def main(input_dir, output_dir, source_name, json_only, text_only):
    """
    Consolidate individual video comment files into single JSON and text files.
    
    Examples:
    
    # Consolidate both JSON and text files
    python flexible_consolidate.py -i "Thailand_output" -o "lancome_Thailand" -s "TikTok @lancomethailand"
    
    # Consolidate only JSON files
    python flexible_consolidate.py -i "Malaysia_output" -o "lancome_Malaysia" --json-only
    
    # Consolidate only text files
    python flexible_consolidate.py -i "Official_output" -o "lancome_Official" --text-only
    """
    
    print(f"🚀 Starting consolidation process...")
    print(f"📂 Input directory: {input_dir}")
    print(f"📁 Output directory: {output_dir}")
    print(f"🏷️ Source name: {source_name}")
    
    # Consolidate JSON files
    if not text_only:
        print(f"\n📊 Consolidating JSON files...")
        json_result = consolidate_json_files(input_dir, output_dir, source_name)
        if not json_result:
            print("⚠️ JSON consolidation failed or no JSON files found")
    
    # Consolidate text files
    if not json_only:
        print(f"\n📝 Consolidating text files...")
        text_result = consolidate_text_files(input_dir, output_dir, source_name)
        if not text_result:
            print("⚠️ Text consolidation failed or no text files found")
    
    print(f"\n🎉 All consolidation tasks completed!")
    print(f"📁 Check the '{output_dir}' directory for results:")
    print(f"   - all_videos_comments.json (consolidated JSON)")
    print(f"   - all_videos_comments.txt (consolidated text)")

if __name__ == "__main__":
    main()
