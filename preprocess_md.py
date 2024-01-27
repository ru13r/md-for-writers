# preprocess_md.py
import sys
import re

def generate_meta(m):
    group2 = m.group(2).strip()
    if group2:
        return f"\n::: meta\n{m.group(3)}\n\n> > *{group2}*\n:::\n\n"
    else:
        return f"\n::: meta\n{m.group(3)}\n:::\n\n"


def preprocess_md(input_file, base_name, no_title=False):
    with open(input_file, 'r') as file:
        content = file.read()

    # Remove the YAML header
    content = re.sub(r'^---[\s\S]*?---\s*', '', content)

    # Remove [!Meta] and [!See also] blocks and their contents
    content = re.sub(r'^>\s*\[!Meta\][\s\S]*?\n\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^>\s*\[!See also\][\s\S]*?\n\n', '', content, flags=re.MULTILINE)

    content = re.sub(r'^\w+::\s*', '', content, flags=re.MULTILINE)
    
    # make extra newlines
    content = content.replace('\n', '\n\n')

    # remove wikipedia style links
    content = re.sub(r'!\[\[([^\]]+)\]\]', '', content)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)

    # Process other custom blocks
    content = re.sub(r'>\s*\[!([a-zA-Z]+)\]([\s\S]*?)\n([\s\S]*?)\n\n', generate_meta, content)

    # Add the title line only if the --no-title argument is not present
    if not no_title:
        processed_content = f"# {base_name}\n{content}"
    else:
        processed_content = content

    # Write to a temporary file
    with open(f"temp_{base_name}.md", 'w') as outfile:
        outfile.write(processed_content)

if __name__ == "__main__":
    # Check if --no-title is the first argument
    no_title = len(sys.argv) > 3 and sys.argv[1] == "--no-title"

    # Adjust indices based on whether --no-title was passed
    input_md = sys.argv[2 if no_title else 1]
    base_md = sys.argv[3 if no_title else 2]

    preprocess_md(input_md, base_md, no_title)