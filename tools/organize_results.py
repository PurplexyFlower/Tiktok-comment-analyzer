import json
import csv
import click

@click.command()
@click.option('--json-file', help='Path to the JSON file')
@click.option('--output-file', help='Path to the output CSV file')
def main(json_file, output_file):
    """
    This script converts a JSON file with TikTok comments to a CSV file.
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['username', 'nickname', 'comment', 'create_time', 'avatar', 'total_reply'])

        # Write comment data
        for comment in data['comments']:
            writer.writerow([
                comment.get('username'),
                comment.get('nickname'),
                comment.get('comment'),
                comment.get('create_time'),
                comment.get('avatar'),
                comment.get('total_reply')
            ])
            
            # Write replies
            if comment.get('replies'):
                for reply in comment.get('replies'):
                    writer.writerow([
                        reply.get('username'),
                        reply.get('nickname'),
                        '    ' + reply.get('comment'), # Indent reply
                        reply.get('create_time'),
                        reply.get('avatar'),
                        reply.get('total_reply')
                    ])

if __name__ == '__main__':
    main()
