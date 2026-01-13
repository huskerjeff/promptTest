#!/usr/bin/env python3
"""
Split PDF by second-level bookmarks (Level 1)
"""
import os
import re
from pypdf import PdfReader, PdfWriter

def sanitize_filename(title):
    """Convert bookmark title to safe filename"""
    # Remove or replace invalid filename characters
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace spaces with underscores
    title = title.replace(' ', '_')
    # Remove leading/trailing dots and spaces
    title = title.strip('. ')
    # Limit length
    if len(title) > 100:
        title = title[:100]
    return title

def get_bookmarks_recursive(bookmarks, level=0, result=None):
    """Recursively extract bookmarks with their levels and page numbers"""
    if result is None:
        result = []

    for item in bookmarks:
        if isinstance(item, list):
            get_bookmarks_recursive(item, level + 1, result)
        else:
            try:
                page = reader.get_destination_page_number(item)
                result.append({
                    'level': level,
                    'title': item.title,
                    'page': page
                })
            except Exception as e:
                print(f"Warning: Could not get page for bookmark: {e}")

    return result

# Read the PDF
input_file = "AI_Engineering_in_Practice_v2_MEAP.pdf"
reader = PdfReader(input_file)
total_pages = len(reader.pages)

print(f"Processing: {input_file}")
print(f"Total pages: {total_pages}")

# Get all bookmarks
bookmarks = reader.outline
all_bookmarks = get_bookmarks_recursive(bookmarks)

# Filter level 1 bookmarks (second level)
level_1_bookmarks = [bm for bm in all_bookmarks if bm['level'] == 1]

print(f"\nFound {len(level_1_bookmarks)} second-level bookmarks")

# Create output directory
output_dir = "split_sections"
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory: {output_dir}\n")

# Split the PDF
for i, bookmark in enumerate(level_1_bookmarks):
    start_page = bookmark['page']

    # Determine end page (next bookmark's page or end of document)
    if i + 1 < len(level_1_bookmarks):
        end_page = level_1_bookmarks[i + 1]['page']
    else:
        end_page = total_pages

    # Create filename
    filename = sanitize_filename(bookmark['title'])
    output_file = os.path.join(output_dir, f"{i+1:02d}_{filename}.pdf")

    # Create PDF writer for this section
    writer = PdfWriter()

    # Add pages for this section
    for page_num in range(start_page, end_page):
        writer.add_page(reader.pages[page_num])

    # Write to file
    with open(output_file, 'wb') as f:
        writer.write(f)

    page_count = end_page - start_page
    print(f"Created: {output_file}")
    print(f"  Pages {start_page + 1}-{end_page} ({page_count} pages)")

print(f"\n✓ Successfully split PDF into {len(level_1_bookmarks)} files")
print(f"  Output directory: {os.path.abspath(output_dir)}")
