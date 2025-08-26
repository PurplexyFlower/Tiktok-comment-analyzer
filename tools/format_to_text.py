import json
import click

@click.command()
@click.option('--json-file', help='Path to the JSON file')
@click.option('--output-file', help='Path to the output text file')
def main(json_file, output_file):
    """
    This script converts a JSON file with TikTok comments to a formatted text file.
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Caption: {data.get('caption')}\n")
        f.write(f"Video URL: {data.get('video_url')}\n")
        f.write("\n" + "="*50 + "\n\n")

        for comment in data['comments']:
            f.write(f"Username: {comment.get('username')}\n")
            f.write(f"Nickname: {comment.get('nickname')}\n")
            f.write(f"Comment: {comment.get('comment')}\n")
            f.write(f"Date: {comment.get('create_time')}\n")
            f.write(f"Avatar: {comment.get('avatar')}\n")
            f.write(f"Total Replies: {comment.get('total_reply')}\n")

            if comment.get('replies'):
                f.write("\n    Replies:\n")
                for reply in comment.get('replies'):
                    f.write("    ----------------------------------------------\n")
                    f.write(f"    Username: {reply.get('username')}\n")
                    f.write(f"    Nickname: {reply.get('nickname')}\n")
                    f.write(f"    Comment: {reply.get('comment')}\n")
                    f.write(f"    Date: {reply.get('create_time')}\n")
                    f.write(f"    Avatar: {reply.get('avatar')}\n")
            
            f.write("\n" + "-"*50 + "\n\n")

if __name__ == '__main__':
    main()
