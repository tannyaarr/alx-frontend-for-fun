#!/usr/bin/python3
"""markdown2html that takes an argument 2 strings"""


import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    """Convert markdown to html"""
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_markdown_file, output_file)

    sys.exit(0)