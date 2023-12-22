# preprocess_md.py
import sys
import re

def preprocess_md(input_file, base_name):
    with open(input_file, 'r') as file:
        content = file.read()

    # Remove the YAML header
    content = re.sub(r'^---[\s\S]*?---\s*', '', content)

    # Remove [!Meta] blocks and their contents
    content = re.sub(r'^>\[!Meta\][\s\S]*?\n\n', '', content, flags=re.MULTILINE)

    content = re.sub(r'^\w+::\s*', '', content, flags=re.MULTILINE)
    
    # make extra newlines
    content = content.replace('\n', '\n\n')

    # remove wikipedia style links
    content = re.sub(r'!\[\[([^\]]+)\]\]', '', content)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)

    # Process other custom blocks
    content = re.sub(r'>\[!([a-zA-Z]+)\]\n([\s\S]*?)\n\n', lambda m: f"\n::: meta\n{m.group(2)}\n:::\n\n", content)


    # Additional processing
    processed_content = f"# {base_name}\n{content}"

    # Write to a temporary file
    with open(f"temp_{base_name}.md", 'w') as outfile:
        outfile.write(processed_content)

if __name__ == "__main__":
    input_md = sys.argv[1]
    base_md = sys.argv[2]
    preprocess_md(input_md, base_md)