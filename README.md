# md-for-writers

This repository contains command line scripts and templates designed for use with Pandoc to generate readable outputs in Word, PDF, and HTML formats, optimized for writers and content creators. All templates are optimized for readability and support Russian language and system TrueType fonts. See [example output](Examples/) for demonstrations of the generated documents.

All instructions are provided for MacOS for default shell `zsh`.

[Русская версия](README_RU.md)

## Installation of Necessary Tools

### Install Pandoc and LaTeX

Pandoc and LaTeX are required for document conversion. Homebrew, a package manager for macOS, is used for installation. LaTeX is specifically needed as a backend for generating PDF files.

```zsh
brew update
brew install pandoc
brew install pdflatex
brew install basictex
```

### Install Additional TeX Packages

Use `tlmgr`, the TeX Live package manager, to install additional packages. These packages provide extended font and language support, and essential LaTeX tools:

- `collection-fontsrecommended`: Provides a collection of recommended fonts for enhanced typography.
- `collection-langcyrillic`: Adds support for Cyrillic scripts, essential for documents in Russian and other languages.
- `latex-tools`: A collection of essential tools and packages for LaTeX processing.
- `tcolorbox`: Provides an environment for colored and framed text boxes with a heading line. Needs `environ` as a dependency. 

```zsh
tlmgr update --self
tlmgr install collection-fontsrecommended
tlmgr install collection-langcyrillic
tlmgr install latex-tools
tlmgr install environ
tlmgr install tcolorbox
```

Note: Run these commands with `sudo` if you encounter permission issues.

## Install the Package

Set up the tool by cloning the repository into the `.pandoc` folder in your home directory and updating your `.zshrc` file to enable the scripts.

```zsh
cd ~
mkdir .pandoc
cd .pandoc
git clone https://github.com/ru13r/md-for-writers.git .
echo "source ~/.pandoc/zsh-scripts" >> ~/.zshrc
```

To activate the changes, restart your terminal or source your `.zshrc`:

```zsh
source ~/.zshrc
```

## Usage

Navigate to the directory containing your Markdown files. Use the following commands to convert your Markdown files into the desired format. Output files will be saved in respective folders (`pdfs`, `html`, or `word`) in the same directory as the source files.

- `mdToPDF file.md`: Converts a specific Markdown file to PDF.
- `mdToHTML file.md`: Converts a specific Markdown file to HTML.
- `mdToWord file.md`: Converts a specific Markdown file to a Word document.

For batch processing, use `*.md` to process all Markdown files in a folder, for example:

```zsh
mdToPDF *.md
```
This command will convert all `.md` files in the current directory to PDF format and save them in the "pdfs" folder.

### `--no-title` option
By default the name of the processed file is added to the output file as the first level header. To supress this behaviour use `--no-title` option: 
```zsh
mdToPDF --no-title your_file.md
```

### Meta section
You may use "Meta" section at the end of your file for notes, comments or sources. It will be ignored when generating the output.
```md
This is output
# Meta
This line and Meta title is ignored.
```


