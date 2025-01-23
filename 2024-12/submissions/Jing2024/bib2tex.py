import os
import re
import bibtexparser

# Function to format authors
def format_authors(authors_raw):
    authors = authors_raw.split(' and ')
    formatted_authors = []

    for author in authors:
        parts = author.split(',')
        last_name = parts[0].strip()
        first_name = parts[1].strip() if len(parts) > 1 else ''

        formatted_name = f"{last_name}, {''.join([name[0].upper() + '.' for name in first_name.split() if name])}"
        formatted_authors.append(formatted_name)

    if len(formatted_authors) > 2:
        return f"{formatted_authors[0]} et al."
    else:
        return ', '.join(formatted_authors)

# Function to format bibitem
def format_bibitem(entry):
    authors = format_authors(entry.get('author', '').replace('\n', ' '))
    title = entry.get('title', '')
    journal = entry.get('journal', '')
    year = entry.get('year', '')
    volume = entry.get('volume', '')
    pages = entry.get('pages', '')
    publisher = entry.get('publisher', '')

    bibitem = f"\\bibitem{{{entry.get('ID', '')}}} {authors}. \n"
    bibitem += f"\\newblock {title}. \n"
    if journal:
        bibitem += f"\\newblock \\emph{{{journal}}}, "
    if volume:
        bibitem += f"{volume}"
    if pages:
        bibitem += f":{pages}"
    if year:
        bibitem += f", {year}."
    if publisher:
        bibitem += f" {publisher}."
    bibitem += "\n"
    return bibitem

# Load BibTeX database
with open('REFER.bib', 'r') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

bib_entries = {entry['ID']: entry for entry in bib_database.entries}

# Set to collect all unique citation keys
all_cited_keys = set()

# Process .tex files to extract all \cite keys
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.tex'):
            tex_file_path = os.path.join(root, file)
            with open(tex_file_path, 'r') as tex_file:
                content = tex_file.read()

            # Ignore comments and find all \cite commands
            content = re.sub(r'(?<!\\)%.*', '', content)  # Remove comments
            citations = re.findall(r'\\cite\{([^}]+)\}', content)
            for cite_block in citations:
                all_cited_keys.update(key.strip() for key in cite_block.split(','))

# Filter valid keys that exist in the BibTeX file
valid_cited_keys = [key for key in all_cited_keys if key in bib_entries]

# Generate the bibliography
formatted_bibliography = "\\begin{thebibliography}{10}\n\\itemsep=1pt\n\\begin{small}\n\n"
for key in valid_cited_keys:
    formatted_bibliography += format_bibitem(bib_entries[key])
formatted_bibliography += "\\end{small}\n\\end{thebibliography}"

# Save to FormattedBibliography.tex
output_path = 'FormattedBibliography.tex'
with open(output_path, 'w') as f:
    f.write(formatted_bibliography)

print(f"Formatted bibliography saved as '{output_path}'.")
