#!/usr/bin/env python3
"""
Examine PDF bookmark structure
"""
from pypdf import PdfReader

def get_bookmarks_recursive(bookmarks, level=0, result=None):
    """Recursively extract bookmarks with their levels and page numbers"""
    if result is None:
        result = []

    for item in bookmarks:
        if isinstance(item, list):
            get_bookmarks_recursive(item, level + 1, result)
        else:
            # item is a Destination object
            title = item.title
            try:
                # Get the page number (0-indexed)
                page = reader.get_destination_page_number(item)
                result.append({
                    'level': level,
                    'title': title,
                    'page': page
                })
            except Exception as e:
                print(f"Warning: Could not get page for bookmark '{title}': {e}")

    return result

# Read the PDF
reader = PdfReader("AI_Engineering_in_Practice_v2_MEAP.pdf")
print(f"Total pages: {len(reader.pages)}")
print(f"\nExtracting bookmarks...\n")

# Get all bookmarks
bookmarks = reader.outline
all_bookmarks = get_bookmarks_recursive(bookmarks)

# Display all bookmarks
print("All bookmarks:")
print("=" * 80)
for bm in all_bookmarks:
    indent = "  " * bm['level']
    print(f"{indent}Level {bm['level']}: '{bm['title']}' -> Page {bm['page'] + 1}")

# Filter level 1 bookmarks (second level, since level 0 is first)
level_1_bookmarks = [bm for bm in all_bookmarks if bm['level'] == 1]

print(f"\n\nSecond-level bookmarks (Level 1, count: {len(level_1_bookmarks)}):")
print("=" * 80)
for bm in level_1_bookmarks:
    print(f"'{bm['title']}' -> Page {bm['page'] + 1}")
